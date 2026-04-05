#  FwMusic v2.1.0W
#  Made by Flying374


import os
import Fwapi_old as LocalAPI
from ttkbootstrap.dialogs import *
import threading
import time
import Fwapi

Supported_api_version = 'v20320'
Api = Fwapi.API()

if Api.get_version() != Supported_api_version:
    print("ErrA1 : LocalAPI Version doesn't match Program version.")
    print('Now the version is :' + Api.get_version() + '.')
    print('Please use :' + Supported_api_version + '.')
    exit()


#  initalization
Flog = Fwapi.FLog()
Flog.create()
downloader = Fwapi.Downloader_v3_Auto()


meter_num1 = LocalAPI.GlobalVar()
meter_num2 = LocalAPI.GlobalVar()
download_numbers = LocalAPI.GlobalVar()

meter_num1.set_value(0)
meter_num2.set_value(0)
download_numbers.set_value(1)


# Main Window
root = ttk.Window(title="FwMusic v2.1.0W", themename="minty", size=(1000, 650), iconphoto='fwl.png')
root.place_window_center()
'''
image = ttk.PhotoImage(file='bg.gif')
background_label = ttk.Label(root, image=image)
background_label.place(relx=0.5, rely=0.5, anchor='center')
'''


variable_value = ttk.StringVar(root)
variable_value.set('0')
variable_music = ttk.BooleanVar(root)
variable_state_meter1 = ttk.StringVar(root)
variable_state_meter2 = ttk.StringVar(root)
variable_state_meter1_text = ttk.StringVar(root)
variable_state_meter2_text = ttk.StringVar(root)
variable_state_meter1.set("dark")
variable_state_meter2.set("dark")
variable_state_meter1_text.set("dark")
variable_state_meter2_text.set("dark")


def download_music_thread():
    type = variable_value.get()
    if type == '0':
        artist_id = search_bar.get()
        artist = Fwapi.Artist(artist_id)
        artist.get_details()
        meter_num1.set_value(100)
        songs = artist.artist_songs
        download_numbers.set_value(len(songs))
        downloader.download(songs, artist.artist_name, do_lyric=False, quality='standard')
    elif type == '1':
        album_id = search_bar.get()
        album = Fwapi.Album(album_id)
        album.get_details()
        songs = album.album_songs
        meter_num1.set_value(100)
        download_numbers.set_value(len(songs))
        downloader.download(songs, album.album_name, do_lyric=False, quality='standard')
    elif type == '2':
        playlist_id = search_bar.get()
        playlist = Fwapi.Playlist_v2(playlist_id)
        playlist.get_details()
        songs = playlist.playlist_songs
        meter_num1.set_value(100)
        download_numbers.set_value(len(songs))
        downloader.download(songs, playlist.playlist_name, do_lyric=False, quality='standard')
    else:
        Messagebox.okcancel(title='Error', message='Please select a type.')

def download_music():
    d = threading.Thread(target=download_music_thread)
    d.start()

def clear():
    search_bar.delete(0, 'end')
    variable_value.set('0')
    meter_num1.set_value(0)
    meter_num2.set_value(0)
    download_numbers.set_value(1)
    variable_state_meter1.set("dark")
    variable_state_meter2.set("dark")
    variable_state_meter1_text.set("dark")
    variable_state_meter2_text.set("dark")





# About Menu
def FwMusic_about():
    Messagebox.okcancel(title='About FwMusic', message='FwMusic is a simple music downloader.'
                                                       '\nThis product is for learning purposes only.\nWe are not '
                                                       'responsible for any consequences resulting from the use of '
                                                       'this product.\nVersion:'
                                                       '2.1.0W(20320+10210)\nAuthor: Flying374.\nTheme:Classic\nFor more '
                                                       'information, please visit: '
                                                       'https://github.com/Flying374/FwMusic2.')


def Author_about():
    Messagebox.okcancel(title='About Me', message='Flying374 is a student with poor grade.\n'
                                                  'Mail: doorofthevoid@qq.com\n'
                                                  'For more information, please visit: '
                                                  'https://github.com/Flying374.')


menubar = ttk.Menu(root)
filemenu = ttk.Menu(menubar)
about = ttk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=about)
about.add_command(label='About FwMusic', command=FwMusic_about)
about.add_command(label='About Me', command=Author_about)
root.config(menu=menubar)

# Main Label
label1 = ttk.Label(root, text="FwMusic", font=('georgia', 50), bootstyle=PRIMARY)

label1.place(relx=0.44, rely=0.09, anchor=CENTER)
label2 = ttk.Label(root, text="v2.1.0W", font=('georgia', 20), bootstyle=PRIMARY)
label2.place(relx=0.71, rely=0.14, anchor=CENTER)


# Search Bar& Button
search_bar = ttk.Entry(root, width=50, font=('georgia', 14), bootstyle=SUCCESS)
search_bar.place(relx=0.48, rely=0.22, anchor=CENTER)
search_button = ttk.Button(root, text="Get", command=download_music,
                           bootstyle=SUCCESS)
search_button.place(relx=0.93, rely=0.22, anchor=CENTER)

select_label = ttk.Label(root, text="Type:", font=('georgia', 14), bootstyle=INFO)
select_label.place(relx=0.05, rely=0.31, anchor=CENTER)
select_button1 = ttk.Radiobutton(root, text="artist", value=0, variable=variable_value, bootstyle=PRIMARY)
select_button1.place(relx=0.2, rely=0.31, anchor=CENTER)
select_button2 = ttk.Radiobutton(root, text="album", value=1, variable=variable_value, bootstyle=PRIMARY)
select_button2.place(relx=0.4, rely=0.31, anchor=CENTER)
select_button3 = ttk.Radiobutton(root, text="playlist(v2)", value=2, variable=variable_value, bootstyle=PRIMARY)
select_button3.place(relx=0.6, rely=0.31, anchor=CENTER)

# meter
meter1 = ttk.Meter(metertype="full", metersize=180, padding=50, amounttotal=100, subtext="Analysising...",
                   subtextstyle="dark", interactive=False,
                   bootstyle='dark', )
meter1.place(relx=0.25, rely=0.68, anchor=CENTER)
meter2 = ttk.Meter(metertype="full", metersize=180, padding=50, amounttotal=download_numbers.get_value(),
                   subtext="Downloading...",
                   subtextstyle="dark", interactive=False,
                   bootstyle='dark', )
meter2.place(relx=0.75, rely=0.68, anchor=CENTER)


label3 = ttk.Label(root, text='No Current Download...', font=('georgia', 14), bootstyle=PRIMARY)
label3.place(relx=0.02, rely=0.95, anchor=W)


# clear button
clear_button = ttk.Button(root, text="Clear", command=clear, bootstyle=DANGER)
clear_button.place(relx=0.48, rely=0.8, anchor=CENTER)


def eexit():
    mb = Messagebox.okcancel(title='Exit', message='Are you sure to exit?')
    # print(mb)
    if mb == 'OK':
        os.system('taskkill /f /im FwMusic.exe')


# Exit Button
exit_button = ttk.Button(root, text="Exit", command=eexit, bootstyle=DANGER)
exit_button.place(relx=0.95, rely=0.95, anchor=CENTER)


def main_upgrade():
    while True:
        meter1.configure(amountused=meter_num1.get_value(), bootstyle=variable_state_meter1.get(),
                         subtextstyle=variable_state_meter1_text.get())
        meter2.configure(amountused=meter_num2.get_value(), bootstyle=variable_state_meter2.get(),
                         subtextstyle=variable_state_meter2_text.get())
        meter2.configure(amounttotal=download_numbers.get_value())
        label3.configure(text='Downloading '+downloader.current_download)
        time.sleep(0.01)
        if downloader.download_total != 0:
            meter_num2.set_value(downloader.download_total)
            variable_state_meter2.set("warning")
            variable_state_meter2_text.set("warning")
        if meter_num1.get_value() != 0:
            variable_state_meter1.set("success")
            variable_state_meter1_text.set("success")
        if meter_num2.get_value() == download_numbers.get_value():
            variable_state_meter2.set("success")
            variable_state_meter2_text.set("success")
            #print('download_numbers',download_numbers.get_value())
            #print('download_numbers',download_numbers.get_value())
            #print('download_numbers',download_numbers.get_value())

        try:
            if search_bar.get() != '':
                int(search_bar.get())
                search_bar.configure(bootstyle=SUCCESS)


        except Exception:
            search_bar.configure(bootstyle=WARNING)



thread1 = threading.Thread(target=main_upgrade)
thread1.start()

root.mainloop()
