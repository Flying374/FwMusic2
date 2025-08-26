import requests
from lxml import etree


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

        except Exception:
            # print('ErrG1')
            return 'ErrG1'
