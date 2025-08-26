#  FwMusic 1.3-dev1
#  Based on 1.1-dev8
import time
import requests
from lxml import etree


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
                    return 'ErrG2'
                self.playlist_songs = self.playlist_songs + playlist_songs
                time.sleep(5)

            except Exception:
                # print('ErrG1')
                return 'ErrG1'