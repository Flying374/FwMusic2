import os


class DataSaver:
    def __init__(self):
        self.type_list = ['Artist', 'Album', 'Playlist']
    def save(self, id, data, type):
        if str(type) not in self.type_list:
            pass  # errsys
        else:
            path = os.path.join('Data', str(type), str(id)+'.txt')
            dir_path = os.path.join('Data', str(type))
            os.makedirs(dir_path, exist_ok=True)
            file = open(path, encoding='utf-8', mode='w+')
            file.write(str(data))
            file.close()
