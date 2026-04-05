#  FwAPI Version : v10203
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
        self.__VersionDictionary = {'API': 'v10203',
                                    'ArtistAPI': '2.0.4(250816)',
                                    'GlobalVarAPI': 'v1.0(250128)',
                                    'ErrInfoAPI': 'v1.0.1(250117)',
                                    'FLogAPI': 'v1.3(250117)',
                                    'PlayListAPI': 'v1.1(250128)',
                                    }

    def get_version(self):
        return self.__VersionDictionary['API']

    def get_version_dictionary(self):
        return self.__VersionDictionary


Api = API()

class GlobalVar:
    def __init__(self):
        self.__value = 0

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def add_value(self, value, stop_time):
        try:
            for i in range(int(value)):
                self.__value += 1
                time.sleep(stop_time)
        except Exception:
            pass
