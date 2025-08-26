import os

import urllib3
import random
import time


class Downloader:
    def __init__(self):
        pass
    def download(self, download_list, artist_name):
        try:
            download_list = []
            os.makedirs(os.path.join('Music'), exist_ok=True)
            os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
            # print(download_list)
            for i in range(len(download_list)):
                if not download_list[i][4]:
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
                    if i // 3 == 0:
                        time.sleep(random.uniform(3, 5))
                    time.sleep(random.uniform(2, 5))
        except Exception:  #errsys
            pass