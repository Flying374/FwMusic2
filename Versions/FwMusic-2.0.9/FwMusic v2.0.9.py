#  FwMusic v2.0.9
#  Made by Flying374
import time
import random
import Fwapi
import threading

api = Fwapi.API()
if api.get_version()[0:4] != 'v203':
    exit('Error:API Version Valid.')

print('FwMusic v2.0.9(20319)')
Lyric = False
Quality_list=['standard', 'higher', 'exhigh', 'lossless', 'hires', 'jyeffect', 'sky', 'jymaster']
Qua = Quality_list[0]
emo = False
flog = Fwapi.FLog()

while True:
    print('Input the type of the song.')
    print('Artist:1  Album:2  Playlist:3  Playlist_v2:4  About:a  Exit:e  config:c self_check:s')
    ans = input('>>>')
    if ans in ['1','2','3','4']:
        download_list = []
        name = 'Default'
        if ans == '1':
            id = input('Artist ID:')
            artist = Fwapi.Artist(id)
            artist.get_details()
            download_list = artist.artist_songs
            name = artist.artist_name


        elif ans == '2':
            id = input('Album ID:')
            album = Fwapi.Album(id)
            album.get_details()
            download_list = album.album_songs
            name = album.album_name # Now

        elif ans == '3':
            id_list = [input('Playlist ID List:')]
            playlist = Fwapi.Playlist(id_list)
            playlist.get_details()
            download_list = playlist.playlist_songs
            name = playlist.playlist_name

        elif ans == '4':
            id = input('Playlist ID:')
            playlist = Fwapi.Playlist_v2(id)
            playlist.get_details()
            download_list = playlist.playlist_songs
            name = playlist.playlist_name

        downloader = Fwapi.Downloader_v3_Auto()
        print('Quality:', Qua)
        print('Lyric:', Lyric)
        if emo:
            print('Enabled Emo Mode.')
            print('Preparing emo comments...')

            def emo():
                net_emo_cloud = Fwapi.NetEmoCloud()
                net_emo_cloud.get_emo_comments(download_list, limit=100)
                emo_list = net_emo_cloud.comment_list_processed
                for i in range(len(emo_list)):
                    print('\n')
                    print(emo_list[i])
                    print('\n')
                    time.sleep(random.uniform(3,5))

            t1 = threading.Thread(target=downloader.download, args=(download_list, name, Qua, Lyric))
            t2 = threading.Thread(target=emo)
            t2.start()
            time.sleep(5)
            t1.start()
        else:
            downloader.download(download_list, name, Qua, Lyric)
        # downloader.download(download_list, name, Qua, Lyric)


    elif ans == 'e':
        flog.exit()
        exit('Bye')


    elif ans == 'c':
        print('Config')
        print('1:---  2:---  3.Quality  4.Lyric  5.Emo')
        a = input('>>>')

        if a == '3':
            qua = input('s-标准, h-较高, eh-极高, l-无损, hi-高清 jye-高清环绕声 sk-沉浸环绕声 jym-超清母带')
            if qua == 's':
                Qua = Quality_list[0]
            elif qua == 'h':
                Qua = Quality_list[1]
            elif qua == 'eh':
                Qua = Quality_list[2]
            elif qua == 'l':
                Qua = Quality_list[3]
            elif qua == 'hi':
                Qua = Quality_list[4]
            elif qua == 'jye':
                Qua = Quality_list[5]
            elif qua =='sk':
                Qua = Quality_list[6]
            elif qua == 'jym':
                Qua = Quality_list[7]

            print('Quality had been set to:', Qua)

        elif a == '4':
            do_lyric = input('Do enable lyric?(T/F):')
            if do_lyric == 'T':
                Lyric = True
            else:
                Lyric = False
            print('Lyric :', Lyric)

        elif a == '5':
            do_emo = input('Do enable Emo Mode?(T/F):')
            if do_emo == 'T':
                emo = True
            else:
                emo = False
            print('Emo Mode :', emo)

        input('<Press Enter to continue.>')


    elif ans == 'a':
        print('FwMusic v2.0.8(20318)')
        print('FwMusic is a music downloader.')
        print('Author: Flying374')
        print('Github: https://github.com/Flying374/FwMusic2')
        print('I am not responsible for any damage caused by this program.')
        input('<Press Enter to continue.>')

    elif ans =='s':
        print('fast/normal/full')
        tp = input('Type:')
        Self_check = Fwapi.Self_Check()
        if tp in ['fast', 'normal', 'full']:
            Self_check.self_check(tp)
        else:
            Self_check.self_check('fast')
        print('Self Check Finished.')
        input('<Press Enter to continue.>')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
