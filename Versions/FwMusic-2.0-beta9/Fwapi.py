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
        self.__VersionDictionary = {'FwMusic_Version': 'v2.0-b9',
                                    'API': 'v20109',
                                    'ArtistAPI': 'v3.0(250701)',
                                    'PlaylistAPI': 'v1.5(250724)',
                                    'PlaylistAPI_v2': 'v2.0(250826)',
                                    'AlbumAPI': 'v1.0(250616)',
                                    'ErrSystem': 'v1.1(250616)',
                                    'FLog': 'v1.4(250616)',
                                    'DataSaver': 'v1.0(250616)',
                                    'Downloader': 'v1.2(250820)',
                                    'Downloader_v2':'v2.0(250820)',
                                    'NcmApiManager': 'v1.0(250726)',
                                    'SimpleApi': 'v1.0(250820)',
                                    'Url': 'v1.0(251007)'
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
        log = open(path, 'a', encoding='utf-8')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') Start FwMusic. Version:' + Api.get_version_dictionary()['FwMusic_Version'] + '\n')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') API Version:' + Api.get_version_dictionary()['API'] + '.' + '\n')

        log.close()

    def info(self, msg):
        path = self.path
        log = open(path, 'a', encoding='utf-8')
        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ')' + str(msg) + '\n')

    def warning(self, msg):
        path = self.path
        log = open(path, 'a', encoding='utf-8')
        log.write('[WARNING] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ')' + str(msg) + '\n')

    def failure(self, msg):
        path = self.path
        log = open(path, 'a', encoding='utf-8')
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
                                'ErrUD3': 'Vip song can not be download.',
                                'ErrA1': "LocalAPI Version doesn't match Program version.",
                                'ErrT1': "Information aren't in right forms.",
                                'ErrD1': 'Fail to analyse music.',
                                'ErrOA1': 'Online Api respond is wrong.'
                                }

    def record(self, ErrType):
        try:
            flog.failure(str(ErrType) + self.__ErrDictionary[ErrType])

        except Exception:
            flog.failure('ErrE1 : ' + self.__ErrDictionary['ErrE1'])
            flog.warning('Unknown Error.')


Errsys = ErrSystem()


class DataSaver:
    def __init__(self):
        self.type_list = ['Artist', 'Album', 'Playlist']

    def save(self, id, data, type):
        if str(type) not in self.type_list:
            Errsys.record('ErrT1')
        else:
            path = os.path.join('Data', str(type), str(id) + '.txt')
            dir_path = os.path.join('Data', str(type))
            os.makedirs(dir_path, exist_ok=True)
            file = open(path, encoding='utf-8', mode='w+')
            file.write(str(data))
            file.close()
            flog.info('Saved data.Type:' + type)


class NcmApiManager:
    def __init__(self):
        self.ApiType = ['api_fast', 'api_slow', 'vip_api']
        self.api_list_fast = ['https://163api.qijieya.cn/',
                              'https://api.sayqz.com/tunefree/ncmapi/',
                              'https://zm.armoe.cn/']
        self.api_list_slow = ['https://apis.netstart.cn/music/',
                              'https://www.musicapi.cn/']
        self.vip_api_list = ['https://www.byfuns.top/api/1/',
                             'https://api.qijieya.cn/meting/']  #  It doesn't work now...

    def GetRandomApi(self, api_type):
        if api_type == 'api_fast':
            return self.api_list_fast[random.randint(0, 2)]
        if api_type == 'api_slow':
            return self.api_list_slow[random.randint(0, 1)]
        if api_type == 'api_vip':
            return 'https://www.byfuns.top/api/1/'  #  use it now...


ncmApiManager = NcmApiManager()


class SimpleApi:
    def format(self, name):
        name = name.replace('/', '-')
        name = name.replace("\ ", '-')
        name = name.replace('|', '-')
        name = name.replace('"', "'")
        name = name.replace(':', '：')
        name = name.replace('?', '？')
        name = name.replace('*', '#')
        name = name.replace('<', '《')
        name = name.replace('>', '》')
        return name


simpleapi = SimpleApi()


class Downloader:
    def __init__(self):
        pass

    def download(self, download_list, artist_name):
        flog.info('Start downloading . Amount:' + str(len(download_list)))
        artist_name = simpleapi.format(artist_name)
        os.makedirs(os.path.join('Music'), exist_ok=True)
        os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
        flog.info('List : ' + str(download_list))
        download_list_new = download_list[:]
        for i in range(len(download_list)):
            if not download_list[i][4]:
                try:
                    print('Downloading music : ' + download_list[i][0])
                    url = 'http://music.163.com/song/media/outer/url?id=' + str(download_list[i][1])
                    # print(url)
                    filename = download_list[i][0]
                    filename = simpleapi.format(filename)
                    connection_pool = urllib3.PoolManager()
                    resp = connection_pool.request('GET', url)
                    # print(str(resp.data[0]) == '60')
                    # print(str(resp.data[-1]) == '62')
                    if str(resp.data[0]) == '60' and str(resp.data[-1]) == '62': # VIP !
                        raise
                    file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                    file.write(resp.data)
                    file.close()
                    resp.release_conn()
                    flog.info('Download music.ID:' + str(download_list[i][1]))
                    # Sleep
                    sleep_time = random.uniform(3, 5)
                    sleep_time += i*random.uniform(0.01, 1/3)
                    if sleep_time >= 12.5:
                        sleep_time = 12.5
                    time.sleep(sleep_time)

                except Exception:
                    download_list_new[i][4] = True
                    flog.warning('Music:' + str(download_list[i][1]) + ' needs vip!')
        return download_list_new


class Downloader_v2:
    try:
        def vip_download(self, download_list, artist_name):
            flog.info('Start downloading . Amount:' + str(len(download_list)))
            artist_name = simpleapi.format(artist_name)
            os.makedirs(os.path.join('Music'), exist_ok=True)
            os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
            flog.info('List : ' + str(download_list))
            download_list_new = download_list[:]
            for i in range(len(download_list_new)):
                if download_list[i][4]:  # Download vip
                    print('Downloading VIP music : ' + download_list[i][0])
                    url = ncmApiManager.GetRandomApi('api_vip') + '?id=' + str(download_list[i][1])
                    # print(url)
                    filename = download_list[i][0]
                    filename = simpleapi.format(filename)
                    connection_pool = urllib3.PoolManager()
                    resp_url = connection_pool.request('GET', url)
                    # print(str(resp_url.data))
                    url_true = resp_url.data.decode('utf-8')
                    # print(url_true)
                    connection_pool.clear()
                    # exit()
                    resp = connection_pool.request('GET', url_true)
                    file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                    file.write(resp.data)
                    file.close()
                    resp.release_conn()
                    flog.info('Download vip music.ID:' + str(download_list[i][1]))
                    # Sleep
                    sleep_time = random.uniform(5, 7)
                    sleep_time += i * random.uniform(0.05, 0.5)
                    if sleep_time >= 25:
                        sleep_time = 25
                    time.sleep(sleep_time)
    except Exception:
        Errsys.record('ErrUD3')


class Artist:
    def __init__(self, artist_id):
        self.artist_id = str(artist_id)
        self.artist_name = 'Default'
        self.artist_songs = []  # [[song_name, song_id, author_name, author_id, is_vip]]

    def get_details(self):
        artist_id = self.artist_id
        try:
            # a:处理完的东西 b:歌曲列表 c:歌曲列表切片 d:歌曲名称 e:歌曲id f:(g的前置项) g:歌单/作者名称 h:作者id i/j:for in range l:单曲作者名称 m:单曲作者id
            page_url = 'https://163api.qijieya.cn/artist/top/song?id=' + str(artist_id)
            Res = requests.request('GET', page_url).text
            Res = Res.replace('true', 'True')
            Res = Res.replace('false', 'False')
            Res = Res.replace('null', "'null'")
            a = eval(Res)
            #  print(a)
            flog.info('Data: \n' + str(a))
            if a['code'] == 200:
                b = a['songs']
                name_list = []
                id_list = []
                for c in b:
                    d = c['name']
                    e = c['id']
                    name_list.append(d)
                    id_list.append(e)
                #  print(b)
                #  f = b[0]['ar'][0]['name']
                f = []
                for i in b:
                    for j in i['ar']:
                        f.append(j['name'])
                #  print(f)
                g = max(f, key=f.count)
                artist_songs = []
                if len(name_list) == len(id_list):
                    for i in range(len(name_list)):
                        artist_songs.append([str(name_list[i]), str(id_list[i]), g, artist_id, False])
                self.artist_id = artist_id
                self.artist_name = g
                self.artist_songs = artist_songs
                flog.info('Succeeded in getting details. Artist id:' + self.artist_id)
            else:
                flog.failure('Api Error. Code:' + str(a['code']))
                Errsys.record('ErrOA1')

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
                    self.playlist_name = html.xpath("//meta[@property='og:title']/@content")[0]
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
                        playlist_songs.append([str(song_names[i]), str(song_ids[i]), 'Unknown', '00000', False])
                else:
                    raise Exception
                self.playlist_songs = self.playlist_songs + playlist_songs
                time.sleep(5)
                flog.info('Succeeded in getting details. Playlist id(s):' + str(self.playlist_id_list))
            except Exception:
                Errsys.record('ErrD1')


class Playlist_v2:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_name = 'Default'
        self.playlist_songs = []  # [[song_name, song_id, author_name, author_id, is_vip]]


    def get_details(self):
        # a:处理完的东西 b:歌曲列表 c:歌曲列表切片 d:歌曲名称 e:歌曲id f:(g的前置项) g:歌单/作者名称 h:作者id i/j:for in range l:单曲作者名称 m:单曲作者id
        playlist_id = self.playlist_id
        try:
            page_url = 'https://163api.qijieya.cn'+'/playlist/track/all?id=' + str(playlist_id)
            page_part_url = 'https://163api.qijieya.cn'+'/playlist/detail?id=' + str(playlist_id)
            Res = requests.request('GET', page_url).text
            Res = Res.replace('true', 'True')
            Res = Res.replace('false', 'False')
            Res = Res.replace('null', "'null'")
            Res_p = requests.request('GET', page_part_url).text
            Res_p = Res_p.replace('true', 'True')
            Res_p = Res_p.replace('false', 'False')
            Res_p = Res_p.replace('null', "'null'")
            a = eval(Res)
            a_p = eval(Res_p)
            # print(a_p)
            flog.info('Data: \n' + str(a))
            if a['code'] == 200 and a_p['code'] == 200:
                b = a['songs']
                name_list = []
                id_list = []
                artist_name_list  = []
                artist_id_list = []
                for c in b:
                    # print(c)
                    d = c['name']
                    e = c['id']
                    l = c['ar'][0]['name']
                    m = c['ar'][0]['id']
                    name_list.append(d)
                    id_list.append(e)
                    artist_name_list.append(l)
                    artist_id_list.append(m)
                g = a_p['playlist']['name']
                playlist_songs = []
                if len(name_list) == len(id_list):
                    for i in range(len(name_list)):
                        playlist_songs.append([str(name_list[i]), str(id_list[i]), str(artist_name_list[i]), str(artist_id_list[i]), False])
                self.playlist_songs = playlist_songs
                self.playlist_name = g
                flog.info('Succeeded in getting details. playlist id:' + str(self.playlist_id))

            else:
                # print('err')
                flog.failure('Api Error. Code:' + str(a['code']))
                Errsys.record('ErrOA1')

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

        except Exception:  # Need ErrInfo
            Errsys.record('ErrD1')


class Url:
    'https://music.163.com/#/artist?id=12520634'
    def __init__(self, url):
        self.url = url

    def get_type(self):
        if 'artist' in self.url:
            return 'artist'
        elif 'album' in self.url:
            return 'album'
        elif 'playlist' in self.url:
            return 'playlist'
        elif 'song' in self.url:
            return'song'
        else:
            return 'unknown'

    def get_id(self):
        url_new = self.url.split('?id=')[-1]
        # print(url_new)
        return url_new


'''
https://163api.qijieya.cn/  Api  
/artist/top/song?id=          Artist Top 50  e.g.12128251(NSZX) 12002038(Wangxiang)
/playlist/track/all?id= &limit=100&offset=1    Playlist 100   e.g.12690395207
Album 目前正常


ar = Artist(54172833)
ar.get_details()
print(ar.artist_songs)
downloader = Downloader()
downloader.download(ar.artist_songs, ar.artist_name)


downloader = Downloader()
downloader.download([['The/*Road:?', '1913206466', 't', 't', False]], 'Test//')
#  16468500 <The Road>  1973672897  2005252136
#  1347264219 月下  1913206466
Downloader  修复


downloader = Downloader_v2()
downloader.vip_download([['The Road:?', '16468500', 't', 't', True]], 'Test//')
Downloader_v2 测试成功


pl_v2 = Playlist_v2(13636082756)
pl_v2.get_details()
print(pl_v2.playlist_songs)
print(pl_v2.playlist_name)
Playlist_v2成功
'''