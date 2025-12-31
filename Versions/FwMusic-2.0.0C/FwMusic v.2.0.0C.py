#  FwMusic v2.0.0C
#  Made by Flying374

import Fwapi

api = Fwapi.API()
if api.get_version()[0:4] != 'v20C':
    exit('Error:API Version Valid.')

print('FwMusic v2.0.0C')
Vip_Api = 'Byfuns'

while True:
    print('Input the type of the song.')
    Enable = input('Do enable VIP Api?(T/F):')
    print('Artist:1  Album:2  Playlist:3  Playlist_v2:4  About:a  Exit:e  config:c')
    ans = input('>>>')
    if ans == '1':
        id = input('Artist ID:')
        artist = Fwapi.Artist(id)
        artist.get_details()
        downloader = Fwapi.Downloader()
        d_n = downloader.download(artist.artist_songs,artist.artist_name)
        if Enable == 'T':
            downloader_v2 = Fwapi.Downloader_v2(Vip_Api)
            downloader_v2.vip_download(d_n, artist.artist_name)

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
        downloader.download(playlist.playlist_songs,playlist.playlist_name)

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
        api_n = input('Vip Api?[B/Q/L]:')
        if api_n == 'B':
            Vip_Api = 'Byfuns'
        elif api_n == 'Q':
            Vip_Api = 'Qijieya'
        elif api_n == 'L':
            Vip_Api = 'Littleyouzi'
        print('Vip Api has been set to:',Vip_Api)
        input('<Press Enter to continue.>')

    elif ans == 'a':
        print('FwMusic v2.0.0C(20C10)')
        print('Author: Flying374')
        print('Github: https://github.com/Flying374/FwMusic2')
        print('I am not responsible for any damage caused by this program.')
        input('<Press Enter to continue.>')

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
