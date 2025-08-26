import time
import tqdm
import random
import urllib3
import requests
from lxml import etree
import os
from werkzeug.http import parse_cookie

# music.163.com/weapi/song/enhance/player/url?id=1455370222&csrf_token=
# http://music.163.com/song/media/outer/url?id=1455370222.mp3
# https://music.163.com/weapi/song/enhance/player/url?csrf_token=
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': 'MUSIC_U=1eb9ce22024bb666e99b6743b2222f29ef64a9e88fda0fd5754714b900a5d70d993166e004087dd3b95085f6a85b059f5e9aba41e3f2646e3cebdbec0317df58c119e5;appver=8.9.75;'
}
'''
'''
入参：artist_id
返回值：[artist_name, artist_id, song_ids, song_names]
'''


class Album:
    def __init__(self, album_id):
        self.album_id = album_id
        self.album_song_list = []  # all songs
        self.album_name = 'Default'

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
            artist_name_xpath = '//*[@data-res-id=' + str(album_id) + ']/@data-res-author'
            artist_name = html.xpath(artist_name_xpath)
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
                    playlist_songs.append([song_names[i], song_ids[i], artist_name[0], '00000', False])
            else:
                return 'ErrG2'
            self.album_song_list = playlist_songs
            time.sleep(5)

        except Exception: # Need ErrInfo
            # print('ErrG1')
            return 'ErrG1'

album_id = 274981737
album = Album(album_id)
album.get_details()
print(album.album_name)
print(album.album_song_list)
print(album.album_id)