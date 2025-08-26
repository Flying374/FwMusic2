#  from:LocalAPI v.10202
#  Author: Flying374
import time
import os


# music.163.com/weapi/song/enhance/player/url?id=1455370222&csrf_token=
# http://music.163.com/song/media/outer/url?id=1455370222.mp3
# https://music.163.com/weapi/song/enhance/player/url?csrf_token=
class API:
    def __init__(self):
        self.__VersionDictionary = {'API': 'v10202',
                                    'ArtistAPI': '2.0.3(250128)',
                                    'GlobalVarAPI': 'v1.0(250128)',
                                    'ErrSystemAPI': 'v1.0.1(250117)',
                                    'FLogAPI': 'v1.3(250117)',
                                    'PlayListAPI': 'v1.1(250128)',
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
                  ') Start FwMusic.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') API Version:' + Api.get_version_dictionary()['API'] + '.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') ArtistAPI Version:' + Api.get_version_dictionary()['ArtistAPI'] + '.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') ErrSystemAPI Version:' + Api.get_version_dictionary()['ErrInfoAPI'] + '.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') FLogAPI Version:' + Api.get_version_dictionary()['FLogAPI'] + '.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') PlayListAPI Version:' + Api.get_version_dictionary()['PlayListAPI'] + '.' + '\n')

        log.write('[INFO] (' + str(time.strftime('%Y-%m-%d %H:%M:%S')) +
                  ') GlobalVarAPI Version:' + Api.get_version_dictionary()['GlobalVarAPI'] + '.' + '\n')

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


class ErrInfo:
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
                                'ErrA1': "LocalAPI Version doesn't match Program version."
                                }

    def record(self, ErrType):
        try:
            flog.failure(str(ErrType) + self.__ErrDictionary[ErrType])

        except Exception:
            flog.failure('ErrE1' + self.__ErrDictionary['ErrE1'])
            flog.warning('Unknown Error.')
