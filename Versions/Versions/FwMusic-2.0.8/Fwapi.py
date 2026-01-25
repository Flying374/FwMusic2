#  FwAPI Version : v20318
#  By Flying374

import random
import time
import os
import requests
import urllib3
from lxml import etree
from playwright.sync_api import sync_playwright


'''
[[song_name, song_id, author_name, author_id, is_vip]]
'''


class API:
    def __init__(self):
        self.__VersionDictionary = {'FwMusic_Version': 'v2.0.8',
                                    'API': 'v20318',
                                    'ArtistAPI': 'v3.0(250701)',
                                    'PlaylistAPI': 'v1.5(250724)',
                                    'PlaylistAPI_v2': 'v2.1.1(251231)',
                                    'AlbumAPI': 'v2.0(260123)',
                                    'ErrSystem': 'v1.1(250616)',
                                    'FLog': 'v1.4(250616)',
                                    'DataSaver': 'v1.0(250616)',
                                    'Downloader': 'v1.2(250820)',
                                    'Downloader_v2': 'v2.2(251203)',
                                    'Downloader_v3_Auto': 'v3.1(260123)',
                                    'NcmApiManager': 'v1.0(250726)',
                                    'SimpleApi': 'v1.0(250820)',
                                    'LyricApi':'v1.0(251231)',
                                    'NetEmoCloud': 'v1.0(251231)',
                                    'Self_Check': 'v1.0(260125)'
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
    def debug(self, msg):
        path = self.path
        log = open(path, 'a', encoding='utf-8')
        log.write('[DEBUG] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
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
                                'ErrOA1': 'Online Api respond is wrong.',
                                'ErrL1': 'Failed to get lyric.'
                                }

    def record(self, ErrType):
        try:
            flog.failure(str(ErrType) +' ' + self.__ErrDictionary[ErrType])

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
        self.api_list_fast = ['https://zm.armoe.cn',
                              'https://163api.qijieya.cn',
                              ]
        self.api_list_slow = ['https://apis.netstart.cn/music',
                              'https://www.musicapi.cn']
        self.vip_api_list = ['http://www.byfuns.top/api/1/?id=',
                             'https://api.qijieya.cn/meting/?type=url&id=']
        self.vip_api_dict = {'Byfuns': 'https://www.byfuns.top/api/1/?id=',
                             'Qijieya': 'https://api.qijieya.cn/meting/?type=url&id='}
        self.vip_api_web_dict = {'cyrui':'https://blog.cyrui.cn/netease/'}

        self.api_list_unable = ['https://api.littleyouzi.com/qq/api/music/net?mid=',
                            'https://ncmapi.btwoa.com']

    def GetRandomApi(self, api_type='api_fast'):
        if api_type == 'api_fast':
            return self.api_list_fast[random.randint(0, len(self.api_list_fast)-1)]
        if api_type == 'api_slow':
            return self.api_list_slow[random.randint(0, len(self.api_list_slow)-1)]
        if api_type == 'api_vip':
            return self.vip_api_list[random.randint(0, len(self.vip_api_list)-1)]

    def GetVipApi(self, api_name):
        if api_name in self.vip_api_dict:
            return self.vip_api_dict[api_name]
        else:
            return self.GetRandomApi('api_fast')


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


class Lyric:
    def __init__(self):
        self.download_id = 0
        self.download_name = ''
        self.lyric = ''
        self.artist_name = 'Default'

    def get_lyric(self, id, name, artist):
        try:
            self.download_id = str(id)
            self.download_name = str(name)
            self.artist_name = str(artist)
            url = ncmApiManager.GetRandomApi('api_fast') + '/lyric?id=' + self.download_id
            res = requests.request('GET', url).text
            res = res.replace('true', 'True')
            res = res.replace('false', 'False')
            res = res.replace('null', "'null'")
            res = eval(res)
            self.lyric = res['lrc']['lyric']
            file = open(os.path.join('Music', self.artist_name, self.download_name + '.lrc'), 'wb')
            file.write(self.lyric.encode('utf-8'))
            file.close()
        except Exception:
            Errsys.record('ErrL1')


lyric = Lyric()


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
                    if str(resp.data[0]) == '60' and str(resp.data[-1]) == '62':  # VIP !
                        raise
                    file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                    file.write(resp.data)
                    file.close()
                    resp.release_conn()
                    flog.info('Download music.ID:' + str(download_list[i][1]))
                    # Sleep
                    sleep_time = random.uniform(3, 5)
                    sleep_time += i * random.uniform(0.01, 1 / 3)
                    if sleep_time >= 12.5:
                        sleep_time = 12.5
                    time.sleep(sleep_time)

                except Exception:
                    download_list_new[i][4] = True
                    flog.warning('Music:' + str(download_list[i][1]) + ' need vip!')
        return download_list_new


class Downloader_v2:
    def __init__(self, api_type):
        self.api_type = api_type
        self.url_true = ''

    def vip_download(self, download_list, artist_name, level='standard'):
        flog.info('Start downloading . Amount:' + str(len(download_list)))
        artist_name = simpleapi.format(artist_name)
        # print(artist_name)
        os.makedirs(os.path.join('Music'), exist_ok=True)
        os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
        flog.info('List : ' + str(download_list))
        download_list_new = download_list[:]
        for i in range(len(download_list_new)):
            try:
                if download_list[i][4]:  # Download vip
                    url = ncmApiManager.GetVipApi(self.api_type) + str(download_list[i][1]) + '&level=' + level
                    print(url)
                    filename = download_list[i][0]
                    filename = simpleapi.format(filename)

                    if self.api_type == 'Byfuns':
                        # print(url)
                        connection_pool = urllib3.PoolManager()
                        resp_url = connection_pool.request('GET', url)
                        # print(str(resp_url.data))
                        self.url_true = resp_url.data.decode('utf-8')
                        # print(url_true)
                        connection_pool.clear()
                        print(self.url_true)

                    elif self.api_type == 'Qijieya':
                        self.url_true = url


                    else:
                        raise Exception
                    print(self.url_true)
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    connection_pool = urllib3.PoolManager()
                    resp = connection_pool.request('GET', self.url_true)
                    file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                    file.write(resp.data)
                    file.close()
                    resp.release_conn()
                    print('Downloading vip music : ', str(download_list[i][0]))
                    flog.info('Download vip music.ID:' + str(download_list[i][1]))
                    # Sleep
                    sleep_time = random.uniform(5, 7)
                    sleep_time += i * random.uniform(0.05, 0.5)
                    if sleep_time >= 25:
                        sleep_time = 25
                    time.sleep(sleep_time)
            except Exception:
                Errsys.record('ErrUD3')


class Downloader_v3_Auto:  # auto
    def __init__(self):
        self.api_type = 'Qijieya'
        self.download_list = []
        self.url_true = ''  # Temp
        self.do_lyric = False

    def download(self, download_list, artist_name, quality='standard', do_lyric=False):
        self.do_lyric = do_lyric
        self.download_list = download_list
        if quality != 'standard':
            self.api_type = 'Byfuns'
        if quality in ['jyeffect', 'sky', 'jymaster']:
            self.api_type = 'Cyrui'
        flog.info('Api has been set to : '+self.api_type)


        if quality == 'standard':
            flog.info('Quality: Standard')
            flog.info('Start normal downloading . Amount:' + str(len(download_list)))
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
                        if str(resp.data[0]) == '60' and str(resp.data[-1]) == '62':  # VIP !
                            raise
                        file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                        file.write(resp.data)
                        file.close()
                        resp.release_conn()
                        flog.info('Download music.ID:' + str(download_list[i][1]))

                        # Lyric
                        if self.do_lyric:
                            lyric.get_lyric(download_list[i][1], filename, artist_name)

                        # Sleep
                        sleep_time = random.uniform(3, 5)
                        sleep_time += i * random.uniform(0.01, 1 / 3)
                        if sleep_time >= 12.5:
                            sleep_time = 12.5
                        time.sleep(sleep_time)

                    except Exception:
                        download_list_new[i][4] = True
                        flog.warning('Music:' + str(download_list[i][1]) + ' need vip!')
            self.download_list = download_list_new

        else:
            flog.info('Start vip/high_quality downloading . Amount:' + str(len(download_list)))
            flog.info('Quality: ' + quality)
            artist_name = simpleapi.format(artist_name)
            # print(artist_name)
            os.makedirs(os.path.join('Music'), exist_ok=True)
            os.makedirs(os.path.join('Music', artist_name), exist_ok=True)
            flog.info('List : ' + str(self.download_list))
            download_list_new = self.download_list[:]
            for i in range(len(download_list_new)):
                try:
                    if download_list[i][4] or quality != 'standard':  # Download vip or high_quality
                        # print(url)
                        filename = download_list[i][0]
                        filename = simpleapi.format(filename)

                        if self.api_type == 'Byfuns':
                            url = ncmApiManager.GetVipApi(self.api_type) + str(download_list[i][1]) + '&level=' + quality
                            # print(url)
                            connection_pool = urllib3.PoolManager()
                            resp_url = connection_pool.request('GET', url)
                            # print(str(resp_url.data))
                            self.url_true = resp_url.data.decode('utf-8')
                            connection_pool.clear()
                            # print(self.url_true)

                        elif self.api_type == 'Qijieya':
                            self.url_true = ncmApiManager.GetVipApi(self.api_type) + str(download_list[i][1])

                        elif self.api_type == 'Cyrui':
                            url = 'http://blog.cyrui.cn/netease/'
                            with sync_playwright() as playwright:
                                browser = playwright.chromium.launch(headless=True)
                                context = browser.new_context(accept_downloads=False)
                                page = context.new_page()
                                page.goto(url)
                                page.fill('input[id="urlInput"]', str(download_list[i][1]))
                                time.sleep(random.uniform(1,2))
                                # Quality
                                Qua = page.query_selector('//*[@id="qualitySelector"]')
                                Qua.click()
                                Qua.select_option(value=quality)
                                time.sleep(random.uniform(0.5, 1.5))
                                get = page.locator('//*[@id="getUrlBtn"]')
                                get.click()
                                time.sleep(random.uniform(5,7))
                                # page.wait_for_load_state('load')
                                download = page.locator('//*[@id="resultDisplay"]/div/div/div[2]/button[2]')
                                while not download.is_visible():
                                    time.sleep(1)
                                with page.expect_event('download') as download_info:
                                    download.click()
                                    download = download_info.value
                                    self.url_true = download.url
                                browser.close()
                                time.sleep(5)

                        else:
                            raise Exception

                        # print(self.url_true)
                        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                        connection_pool = urllib3.PoolManager()
                        resp = connection_pool.request('GET', self.url_true)
                        file = open(os.path.join('Music', artist_name, filename + '.mp3'), 'wb')
                        file.write(resp.data)
                        file.close()
                        resp.release_conn()
                        print('Downloading vip/high_quality music : ', str(download_list[i][0]))
                        flog.info('Download vip/high_quality music.ID:' + str(download_list[i][1]))

                        # Lyric
                        if self.do_lyric:
                            print('lyric downloading')
                            lyric.get_lyric(download_list[i][1], filename, artist_name)

                        # Sleep
                        sleep_time = random.uniform(5, 7)
                        sleep_time += i * random.uniform(0.05, 0.5)
                        if sleep_time >= 25:
                            sleep_time = 25
                        time.sleep(sleep_time)

                except Exception:
                    Errsys.record('ErrUD3')


class NetEmoCloud:
    def __init__(self):
        self.song_id_list = []
        self.comment_list_unprocessed = []
        self.comment_list_processed = []
        self.__emo_words_v1 = [
    '丧', '伤感', '忧郁', '孤独', '遗憾', '心碎', '眼泪', '深渊', '失落', '痛苦',
    '压抑', '消沉', '焦虑', '沉闷', '破碎', '窒息', '绝望', '空虚', '麻木', '无力',
    '深夜', '凌晨', '雨天', '阴天', '背影', '路灯', '耳机', '失眠', '旧照', '残花',
    '伤口', '结痂', '刺', '针', '幽灵', '黑洞', '溺亡', '灰烬', '枯叶', '断线',
    '多余', '废物', '卑微', '可笑', '活该', '抱歉', '亏欠', '累赘', '迷失', '溃败',
    '再见', '走散', '过期', '未读', '拉黑', '退场', '失约', '过期', '逾期', '遗落',
    '强颜欢笑', '撕心裂肺', '如鲠在喉', '万箭穿心', '不告而别', '杳无音讯',
    '无人问津', '油尽灯枯', '覆水难收', '一病不起', '无疾而终', '苟延残喘',
    '清醒着沉沦', '笑着流眼泪', '比哭难看的笑', '不被需要的我',
    '凌晨三点', '回忆', '袭击', '快乐需要演技', '心脏骤停瞬间',
    '灰烬', '吹散', '没有结局',
    '谎言', '已读不回', '欲言又止', '到此为止', '不再联系',
    '不喜欢'
    ]


    def get_emo_comments(self, id_list, limit=100):
        times = 0
        for detail in id_list:
            if times <= limit:
                url = 'https://music.163.com/api/v1/resource/comments/R_SO_4_' + str(detail[1]) + '?limit=50&offset=0'
                response = str(requests.get(url).text)
                response = response.replace('false', 'False')
                response = response.replace('true', 'True')
                response = response.replace('null', '""')
                a = eval(response)
                # print(a)
                try:
                    for i in range(50):
                        comment = a['hotComments'][i]['content']
                        self.comment_list_unprocessed.append(comment)
                        for emo_word in self.__emo_words_v1:
                            if emo_word in comment:
                                self.comment_list_processed.append(comment)

                except IndexError:
                    time.sleep(random.uniform(1, 3))
                    pass
                times+= 1

        # print(self.comment_list_unprocessed)
        # print(self.comment_list_processed)


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
            ncmapi = ncmApiManager.GetRandomApi('api_fast')
            flog.info('Getting details.')
            flog.info('Api :' + ncmapi)
            page_url = ncmapi + '/playlist/track/all?id=' + str(playlist_id) + '&limit=1000&offset=0'
            page_part_url = ncmapi + '/playlist/detail?id=' + str(playlist_id)
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
                artist_name_list = []
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
                        playlist_songs.append(
                            [str(name_list[i]), str(id_list[i]), str(artist_name_list[i]), str(artist_id_list[i]),
                             False])
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
        self.album_songs = []  # all songs
        self.album_name = 'Default'
        self.artist_name = 'Unknown'

    def get_details(self):
        album_id = self.album_id
        # try:
        try:
            # a:处理完的东西 b:歌曲列表 c:歌曲列表切片 d:歌曲名称 e:歌曲id f:(g的前置项) g:歌单/作者名称 h:作者id i/j:for in range l:单曲作者名称 m:单曲作者id
            page_url = ncmApiManager.GetRandomApi('api_fast') + '/album?id=' + str(album_id)
            Res = requests.request('GET', page_url).text
            Res = Res.replace('true', 'True')
            Res = Res.replace('false', 'False')
            Res = Res.replace('null', "'null'")
            a = eval(Res)
            # print(a)
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
                # print(b)
                f = b[0]['al']['name']
                # f = []
                # for i in b:
                #     for j in i['ar']:
                #        f.append(j['name'])
                # g = max(f, key=f.count)
                album_songs = []
                # print(len(name_list), len(id_list), len(f))
                if len(name_list) == len(id_list):
                    for i in range(len(name_list)):
                        #print(str(name_list[i]), str(id_list[i]), 'Unknown', '00000', False)
                        album_songs.append([str(name_list[i]), str(id_list[i]), 'Unknown', '00000', False])
                self.album_id = album_id
                self.album_name = f
                self.album_songs = album_songs
               # print(self.album_songs)
                flog.info('Succeeded in getting details. Album id:' + str(self.album_id))
            else:
                flog.failure('Api Error. Code:' + str(a['code']))
                Errsys.record('ErrOA1')

        except Exception:
             Errsys.record('ErrD1')


class Self_Check:
    def __init__(self):
        self.type = 'full'

    def self_check(self, type):
        self.type = type
        flog.debug('Starting self check.Type:' + str(self.type))
        if self.type == 'fast' or self.type == 'normal' or self.type == 'full':
            flog.debug('Checking versions...')
            version_dictionary = Api.get_version_dictionary()
            for api, version in version_dictionary.items():
                flog.debug(api + ' : ' + version)

        if self.type == 'normal'or self.type == 'full':
            d = Downloader_v3_Auto()
            ncmapifast = ncmApiManager.api_list_fast
            flog.debug('Testing NcmApis...')
            for apis in ncmapifast:
                url = apis + '/song/detail?ids=2041814115'
                Res = requests.request('GET', url).text
                Res = Res.replace('true', 'True')
                Res = Res.replace('false', 'False')
                Res = Res.replace('null', "'null'")
                a = eval(Res)
                if a['songs'][0]['name'] == '走过漫漫时空':
                    flog.debug('Api:' + apis +'is valid.')
                else:
                    flog.failure('Api:' + apis +' is NOT valid.')
                # print(a)
        if self.type == 'full':
            flog.debug('Checking FwApi...')

            ar_c = Artist('12094419')
            ar_c.get_details()
            # print(len(ar_c.artist_songs))
            if ar_c.artist_name == '羽肿' and len(ar_c.artist_songs)>=16:
                flog.debug('FwApi.Artist is valid.')
            else:
                flog.failure('FwApi.Artist is NOT valid.')

            pl_v2_c = Playlist_v2(8743547907)
            pl_v2_c.get_details()
            if len(pl_v2_c.playlist_songs)>=1:
                flog.debug('FwApi.Playlist_v2 is valid.')
            else:
                flog.failure('FwApi.Playlist_v2 is NOT valid.')

            al_c = Album(34856396)
            al_c.get_details()
            if len(al_c.album_songs)==1 and al_c.album_name=='Windy Hill':
                flog.debug('FwApi.Album is valid.')
            else:
                flog.failure('FwApi.Album is NOT valid.')


        flog.info('Debug Finished.')



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


downloader = Downloader_v2('ByFuns')
downloader.vip_download([['Windy Hill', '427606780', 'test','unknown', True]], 'Test')
# Downloader_v2 测试成功


pl_v2 = Playlist_v2(13636082756)
pl_v2.get_details()
print(pl_v2.playlist_songs)
print(pl_v2.playlist_name)
Playlist_v2成功
'''
'''
id = 12277194
g = Artist(12277194)
g.get_details()
print(g.artist_songs)
d = Downloader_v3_Auto()
d.download(g.artist_songs, g.artist_name, 'exhigh', True)

pl = Playlist_v2('941306349')
pl.get_details()
net_emo_cloud = NetEmoCloud()
net_emo_cloud.comment(pl.playlist_songs, 20)

album = Album(164274913)
album.get_details()
print(album.album_name)
print(album.album_songs)
'''