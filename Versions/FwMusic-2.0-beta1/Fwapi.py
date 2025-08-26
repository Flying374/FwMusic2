#  FwAPI Version : v2.0.0
#  By Flying374

import random
import time
import os
import requests
import urllib3
from lxml import etree


'''
[[song_name, song_id, author_name, author_id, is_vip]]
'''


class API:
    def __init__(self):
        self.__VersionDictionary = {'FwMusic_Version':'v2.0-b1',
                                    'API': 'v20000',
                                    'ArtistAPI': 'v2.1(250616)',
                                    'PlaylistAPI':'v1.4(250616)',
                                    'AlbumAPI':'v1.0(250616)',
                                    'ErrSystem': 'v1.1(250616)',
                                    'FLog': 'v1.4(250616)',
                                    'DataSaver': 'v1.0(250616)',
                                    'Downloader':'v.1.1(250616)'
                                    }

    def get_version(self):
        return self.__VersionDictionary['API']

    def get_version_dictionary(self):
        return self.__VersionDictionary


Api = API()


class FLog:
    def __init__(self):
        self.log_time = str(time.strftime('%Y-%m-%d-%H-%M-%S'))
        self.path = os.path.join('Logs', self.log_time + '.txt')

    def create(self):
        os.makedirs('Logs', exist_ok=True)
        path = self.path
        log = open(path, 'a')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') Start FwMusic. Version:' + Api.get_version_dictionary()['FwMusic_Version'] + '\n')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') API Version:' + Api.get_version_dictionary()['API'] + '.' + '\n')

        log.close()

    def info(self, msg):
        path = self.path
        log = open(path, 'a')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ')' + str(msg) + '\n')

    def warning(self, msg):
        path = self.path
        log = open(path, 'a')
        log.write('[WARNING] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ')' + str(msg) + '\n')

    def failure(self, msg):
        path = self.path
        log = open(path, 'a')
        log.write('[FAILURE] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ')' + str(msg) + '\n')


flog = FLog()
flog.create()


class ErrSystem:
    def __init__(self):
        self.__ErrDictionary_old = {'ErrR1': 'File does NOT exist.',
                                    'ErrG1': 'Fail to get details from (https://music.163.com/#/artist?id=).',
                                    'ErrG2': "Information aren't in right forms.",
                                    'ErrE1': 'Error type is not in list.',
                                    'ErrA1': "LocalAPI Version doesn't match Program version.",
                                    'ErrUD1': 'Can not download music from 163music.',
                                    'ErrPL1': 'Artist file does NOT exist.',
                                    'ErrAD1': 'Fail to download music from 163music.',
                                    }
        self.__ErrDictionary = {'ErrE1': 'Error type is not in list.',
                                'ErrUD1': 'Can not download music from 163music.',
                                'ErrUD2': 'Songs require vip.',
                                'ErrA1': "LocalAPI Version doesn't match Program version.",
                                'ErrT1': "Information aren't in right forms.",
                                'ErrD1': 'Fail to analyse music.'
                                }

    def record(self, ErrType):
        try:
            flog.failure(str(ErrType) + self.__ErrDictionary[ErrType])

        except Exception:
            flog.failure('ErrE1' + self.__ErrDictionary['ErrE1'])
            flog.warning('Unknown Error.')


Errsys = ErrSystem()


class DataSaver:
    def __init__(self):
        self.type_list = ['Artist', 'Album', 'Playlist']
    def save(self, id, data, type):
        if str(type) not in self.type_list:
            Errsys.record('ErrT1')
        else:
            path = os.path.join('Data', str(type), str(id)+'.txt')
            dir_path = os.path.join('Data', str(type))
            os.makedirs(dir_path, exist_ok=True)
            file = open(path, encoding='utf-8', mode='w+')
            file.write(str(data))
            file.close()
            flog.info('Saved data.Type:'+type)


class Downloader:
    def download(self, download_list, artist_name):
        flog.info('Start downloading.Amount:' + str(len(download_list)))
        try:
            os.makedirs(os.path.join('Music'), exist_ok=True)
            os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
            # print(download_list)
            for i in range(len(download_list)):
                if not download_list[i][4]:
                    print('Downloading music:'+download_list[i][0])
                    url = 'http://music.163.com/song/media/outer/url?id=' + str(download_list[i][1])
                    # print(url)
                    filename = download_list[i][0]
                    filename.replace('/', '-')
                    filename.replace(':', '：')
                    filename.replace('!', '!')
                    filename.replace('?', '？')
                    filename.replace('.', '。')
                    filename.replace('<', '《')
                    filename.replace('>', '》')
                    connection_pool = urllib3.PoolManager()
                    resp = connection_pool.request('GET', url)
                    file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                    file.write(resp.data)
                    file.close()
                    resp.release_conn()
                    flog.info('Download music.ID:' + download_list[i][1])
                    if i // 3 == 0:
                        time.sleep(random.uniform(3, 5))
                    time.sleep(random.uniform(2, 5))
        except Exception:  #errsys
            Errsys.record('ErrUD1')


class Artist:
    def __init__(self, artist_id):
        self.artist_id = artist_id
        self.artist_name = 'Default'
        self.artist_songs = []  # [[song_name, song_id, author_name, author_id, is_vip]]


    def get_details(self):
        artist_id = self.artist_id

        try:
            headers = {
                'Referer': 'http://music.163.com',
                'Host': 'music.163.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'User-Agent': 'Chrome/10'
            }
            page_url = 'https://music.163.com/artist?id=' + str(artist_id)  # no/#/, it's a bug
            res = requests.request('GET', page_url, headers=headers)
            html = etree.HTML(res.text)
            artist_name = html.xpath("//meta[@name='keywords']/@content")[0]
            href_xpath = "//*[@id='hotsong-list']//a/@href"
            name_xpath = "//*[@id='hotsong-list']//a/text()"
            hrefs = html.xpath(href_xpath)
            names = html.xpath(name_xpath)
            song_ids = []
            song_names = []
            # print(song_ids, song_names)  # debug only
            for href, name in zip(hrefs, names):
                song_ids.append(href[9:])
                song_names.append(name)
                # print(href, ' ', name)  # debug only
            artist_songs = []
            if len(song_names) == len(song_ids):
                for i in range(len(song_names)):
                    artist_songs.append([song_names[i], song_ids[i], artist_name, artist_id, False])
            else:
                pass
            self.artist_id = artist_id
            self.artist_name = artist_name
            self.artist_songs = artist_songs
            flog.info('Succeeded in getting details. Artist id:' + self.artist_id)

        except Exception:
            Errsys.record('ErrD1')


class Playlist:
    def __init__(self, playlist_id_list):
        self.playlist_id_list = playlist_id_list
        self.playlist_name = 'Default'
        self.playlist_songs = []  # [[song_name, song_id, author_name, author_id, is_vip]]


    def get_details(self):
        playlist_id_list = self.playlist_id_list
        for i in range(len(playlist_id_list)):
            try:
                headers = {
                    'Referer': 'http://music.163.com',
                    'Host': 'music.163.com',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'User-Agent': 'Chrome/10'
                }
                page_url = 'https://music.163.com/playlist?id=' + str(playlist_id_list[i])  # no/#/, it's a bug
                res = requests.request('GET', page_url, headers=headers)
                html = etree.HTML(res.text)
                if i == 0:
                    self.playlist_name = html.xpath("//meta[@property='og:title']/@content")
                href_xpath = "//*[@id='song-list-pre-cache']//a/@href"
                name_xpath = "//*[@id='song-list-pre-cache']//a/text()"
                hrefs = html.xpath(href_xpath)
                names = html.xpath(name_xpath)
                song_ids = []
                song_names = []
                # print(song_ids, song_names)  # debug only
                for href, name in zip(hrefs, names):
                    song_ids.append(href[9:])
                    song_names.append(name)
                    # print(href, ' ', name)  # debug only
                playlist_songs = []
                if len(song_names) == len(song_ids):
                    for i in range(len(song_names)):
                        playlist_songs.append([song_names[i], song_ids[i], 'Unknown', '00000', False])
                else:
                    raise Exception
                self.playlist_songs = self.playlist_songs + playlist_songs
                time.sleep(5)
                flog.info('Succeeded in getting details. Playlist id:' + self.playlist_id_list)
            except Exception:
                Errsys.record('ErrD1')


class Album:
    def __init__(self, album_id):
        self.album_id = album_id
        self.album_song_list = []  # all songs
        self.album_name = 'Default'
        self.artist_name = 'Unknown'

    def get_details(self):
        try:
            headers = {
                'Referer': 'http://music.163.com',
                'Host': 'music.163.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'User-Agent': 'Chrome/10'
            }
            page_url = 'https://music.163.com/album?id=' + str(self.album_id)  # no/#/, it's a bug
            res = requests.request('GET', page_url, headers=headers)
            html = etree.HTML(res.text)
            self.album_name = html.xpath("//meta[@property='og:title']/@content")[0]
            href_xpath = "//*[@id='song-list-pre-cache']//a/@href"
            name_xpath = "//*[@id='song-list-pre-cache']//a/text()"
            artist_name_xpath = '//*[@data-res-id=' + str(self.album_id) + ']/@data-res-author'
            self.artist_name = html.xpath(artist_name_xpath)[0]
            hrefs = html.xpath(href_xpath)
            names = html.xpath(name_xpath)

            song_ids = []
            song_names = []
            for href, name in zip(hrefs, names):
                song_ids.append(href[9:])
                song_names.append(name)
            playlist_songs = []
            if len(song_names) == len(song_ids):
                for i in range(len(song_names)):
                    playlist_songs.append([song_names[i], song_ids[i], self.artist_name[0], '00000', False])
            else:
                raise Exception
            self.album_song_list = playlist_songs
            time.sleep(5)
            flog.info('Succeeded in getting details. Album id:' + self.album_id)

        except Exception: # Need ErrInfo
            Errsys.record('ErrD1')