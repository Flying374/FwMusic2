#  FwMusic v2.0.5
#  Made by Flying374

import Fwapi
import os

api = Fwapi.API()
if api.get_version()[0:4] != 'v203':
    exit('Error:API Version Valid.')

print('FwMusic v2.0.5')
Vip_Api = 'Byfuns'
Enable = 'F'
Quality_list=['standard', 'higher', 'exhigh', 'lossless', 'hires']
Qua = Quality_list[0]

'''
while True:
    print('Input the type of the song.')
    # Enable = input('Do enable VIP Api?(T/F):')
    print('Artist:1  Album:2  Playlist:3  Playlist_v2:4  About:a  Exit:e  config:c')
    ans = input('>>>')
    if ans == '1':
        id = input('Artist ID:')
        artist = Fwapi.Artist(id)
        artist.get_details()
        if Qua == 'standard':
            downloader = Fwapi.Downloader()
            d_n = downloader.download(artist.artist_songs, artist.artist_name)
            if Enable == 'T':
                downloader_v2 = Fwapi.Downloader_v2(Vip_Api)
                downloader_v2.vip_download(d_n, artist.artist_name)
        else:
            # print(artist.artist_songs)
            new = []
            for i in artist.artist_songs:
                i[4] = True
                new.append(i)
            print('Quality:', Qua)
            Vip_Api = 'Byfuns'
            downloader_v2 = Fwapi.Downloader_v2(Vip_Api)
            downloader_v2.vip_download(new, artist.artist_name, Qua)



    elif ans == '2':
        id = input('Album ID:')
        album = Fwapi.Album(id)
        album.get_details()
        downloader = Fwapi.Downloader()

        d_n = downloader.download(album.album_song_list, album.album_name)
        if Enable == 'T':
            downloader_v2 = Fwapi.Downloader_v2(Vip_Api)
            downloader_v2.vip_download(d_n, album.album_name)

    elif ans == '3':
        id_list = [input('Playlist ID List:')]
        playlist = Fwapi.Playlist(id_list)
        playlist.get_details()
        downloader = Fwapi.Downloader()
        downloader.download(playlist.playlist_songs, playlist.playlist_name)

    elif ans == '4':
        id = input('Playlist ID:')
        playlist = Fwapi.Playlist_v2(id)
        playlist.get_details()
        downloader = Fwapi.Downloader()
        d_n = downloader.download(playlist.playlist_songs, playlist.playlist_name)
        if Enable == 'T':
            downloader_v2 = Fwapi.Downloader_v2(Vip_Api)
            downloader_v2.vip_download(d_n, playlist.playlist_name)

    elif ans == 'e':
        exit('Bye')

    elif ans == 'c':
        print('Config')
        print('1:Enable VIP Api  2:Set VIP Api 3. Quality')
        a = input('>>>')
        if a == '1':
            enable = input('Enable VIP Api?(T/F):')
            if enable == 'T':
                Enable = 'T'
            else:
                Enable = 'F'
            print('VIP Api has enabled:', Enable)
        elif a == '2':
            api_n = input('Vip Api?[B/Q]:')
            if api_n == 'B':
                Vip_Api = 'Byfuns'
            elif api_n == 'Q':
                Vip_Api = 'Qijieya'
            #elif api_n == 'L':
            #    Vip_Api = 'Littleyouzi'
            print('Vip Api has been set to:', Vip_Api)
        elif a == '3':
            qua = input('s-标准, h-较高, eh-极高, l-无损, hi-高清')
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
            print('Quality had been set to:', Qua)

        input('<Press Enter to continue.>')

    elif ans == 'a':
        print('FwMusic v2.0.3(20213)')
        print('Author: Flying374')
        print('Github: https://github.com/Flying374/FwMusic2')
        print('I am not responsible for any damage caused by this program.')
        input('<Press Enter to continue.>')

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
'''

downloader = Fwapi.Downloader_v3_Auto()
id = 9944
artist = Fwapi.Artist(id)
artist.get_details()
downloader_v3 = Fwapi.Downloader_v3_Auto()
downloader_v3.download(artist.artist_songs, artist.artist_name, 'higher', True)
