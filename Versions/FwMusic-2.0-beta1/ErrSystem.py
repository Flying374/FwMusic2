#  From: LocalAPI v.10202
#  Author: Flying374
class ErrInfo:
    def __init__(self):
        self.__ErrDictionary = {'ErrR1': 'File does NOT exist.',
                                'ErrG1': 'Fail to get details from (https://music.163.com/#/artist?id=).',
                                'ErrG2': "Information aren't in right forms.",
                                'ErrE1': 'Error type is not in list.',
                                'ErrA1': "LocalAPI Version doesn't match Program version.",
                                'ErrUD1': 'Can not download music from 163music.',
                                'ErrPL1': 'Artist file does NOT exist.',
                                'ErrAD1': 'Fail to download music from 163music.',
                                }

    def solve(self, ErrType):
        try:
            return self.__ErrDictionary[ErrType]

        except Exception:
            return 'ErrE1'