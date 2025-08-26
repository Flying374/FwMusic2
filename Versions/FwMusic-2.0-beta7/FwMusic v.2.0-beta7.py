#  FwMusic v2.0-beta7
#  Made by Flying374

import Fwapi

api = Fwapi.API()
if api.get_version()[0:4] != 'v200':
    exit('Error:API Version Valid.')

print('FwMusic v2.0-beta7')

while True:
    print('Input the type of the song.')
    print('Artist:1  Album:2  Playlist:3 Exit:e')
    ans = input('>>>')
    if ans == '1':
        id = input('Artist ID:')
        artist = Fwapi.Artist(id)
        artist.get_details()
        downloader = Fwapi.Downloader()
        downloader.download(artist.artist_songs,artist.artist_name)
    elif ans == '2':
        id = input('Album ID:')
        album = Fwapi.Album(id)
        album.get_details()
        downloader = Fwapi.Downloader()
        downloader.download(album.album_song_list, album.album_name)
    elif ans == '3':
        id_list = [input('Artist ID List:')]
        playlist = Fwapi.Playlist(id_list)
        playlist.get_details()
        downloader = Fwapi.Downloader()
        downloader.download(playlist.playlist_songs,playlist.playlist_name)
    elif ans == 'e':
        exit('Bye')
    print('\n\n\n\n\n\n\n\n\n\n')