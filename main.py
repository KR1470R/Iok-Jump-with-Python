#################################################--START--#############################################
from PIL import ImageTk, Image 
from tkinter import *
import tkinter as tk
import os
import signal
import sys
from pygame import mixer
from galaxy import main_galaxy
from sky import main_sky
from threading import Thread

my_coin = open("My_Coin.txt", "r")
coins = my_coin.read()
my_coin.close()

PATH_TO_MUSIC = os.path.abspath('media/music/background_msc.mp3')

FONT_NAME = ''

def settings_icon():
    global settings
    if w == 1920 and h == 1080:
        path_to_settings = os.path.abspath('media/screen_resolution/1920_1080/main_menu/settings.png')
        settings_icon = PhotoImage(file=path_to_settings)
        settings = Label(image=settings_icon,bg='#3B4EA3',cursor='hand1')
        settings.image = settings_icon
        settings.place(relx=1,rely=0.0,anchor=NE)
        settings.bind('<Button-1>',open_settings)
    
    elif w == 1366 or 1360 and h == 768:
        path_to_settings = os.path.abspath('media/screen_resolution/1366_768/main_menu/settings.png')
        settings_icon = PhotoImage(file=path_to_settings)
        settings = Label(image=settings_icon,bg='#3B4EA3',cursor='hand1')
        settings.image = settings_icon
        settings.place(relx=1,rely=0.0,anchor=NE)
        settings.bind('<Button-1>',open_settings)

def volume_icon():
    path_to_off = os.path.abspath('media/settings/volume_off.png')
    volume_off_1 = PhotoImage(file=path_to_off)
    analyze_for_music = open('configs/music_file.txt')
    readed=analyze_for_music.read()
    def stop_music():
        mixer.init()
        music_file = open('configs/music_file.txt','w+')
        music_file.write('False')
        music_file.close()
        mixer.music.stop()
    def volume_off(event):
        stop_music()
        volume_galka.config(image=volume_off_1)
        volume_galka.bind('<Button-1>',volume_on_1)
    def start_music():
        music_file = open('configs/music_file.txt','w+')
        music_file.write('True')  
        music_file.close()
        mixer.init()
        mixer.music.load(PATH_TO_MUSIC)
        mixer.music.play(-1, 0.0)
    def volume_on_1(event):
        volume_galka.config(image=volume_icon_1)
        volume_galka.bind('<Button-1>',volume_off)
        start_music()
    def play_music():
        global music_file
        music_file_for_read = open('configs/music_file.txt','r')
        readed = music_file_for_read.read()
        print(readed)
        if readed == 'False':
            stop_music()
            volume_galka.config(image=volume_off_1)
            volume_galka.bind('<Button-1>',volume_on_1)
        else:
            music_file = open('configs/music_file.txt','w+')
            music_file.write('True')  
            music_file.close()
            mixer.init()
            mixer.music.load(PATH_TO_MUSIC)
            mixer.music.play(-1, 0.0)

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    if w == 1920 and h == 1080: 
        path_volume = os.path.abspath('media/settings/volume_on.png')
        volume_icon_1 = PhotoImage(file=path_volume)
        volume_galka = Label(image=volume_icon_1,bg='#3B4EA3',cursor='hand1')
        volume_galka.bind('<Button-1>',volume_off)
        volume_galka.image = volume_icon_1
        volume_galka.place(x=1800)
    elif w == 1360 and h == 768:
        path_volume = os.path.abspath('media/settings/volume_on.png')
        volume_icon_1 = PhotoImage(file=path_volume)
        volume_galka = Label(image=volume_icon_1,bg='#3B4EA3',cursor='hand1')
        volume_galka.bind('<Button-1>',volume_off)
        volume_galka.image = volume_icon_1
        volume_galka.place(x=1250)
    play_music()
def play_with_game():
    music = Thread(target=volume_icon)
    music.start()
    game = Thread(target=main)
    game.start()

def play_music_with_game(event):
    game = Thread(target=main)
    game.start()
    music = Thread(target=play_music)
    music.start()

def window():
    global root
    global w, h
    global label
    global button 
    global button_exit
    global settings

    root = Tk()
    root.resizable(False, False)

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    def main_window():
        global button
        global button_shop
        global button_exit
        global label
        global coin_icon_spawn
        global for_menu

        if w == 1920 and h == 1080:
            def glavy(event):
                global glava_1 
                global glava_2 
                global choose_label
                remove_all()

                path_to_button_home = os.path.abspath('media/game_icons/home.png')
                button_home_lbl_icon = PhotoImage(file=path_to_button_home)
                button_home_lbl_icon.image = button_home_lbl_icon
                button_home_lbl = Label(root,image=button_home_lbl_icon,cursor='hand1',bg='#3B4EA3')
                button_home_lbl.place(relx=0.90,rely=0.04,anchor=CENTER)
                button_home_lbl.bind('<Button-1>',back_home)

                #sky glava
                path_to_sky_icon = os.path.abspath('media/screen_resolution/1920_1080/main_menu/glavy/sky_glava/sky.png')
                sky_icon = PhotoImage(file=path_to_sky_icon)
                glava_1 = Label(image=sky_icon,bg='#3B4EA3',cursor='hand1')
                glava_1.image = sky_icon
                glava_1.place(relx=0.5,rely=0.4,anchor=CENTER)
                glava_1.bind('<Button-1>', main_sky)
                
                #galaxy glava 
                path_to_galaxy_icon = os.path.abspath('media/screen_resolution/1920_1080/main_menu/glavy/galaxy_glava/galaxy.png')
                galaxy_icon = PhotoImage(file=path_to_galaxy_icon)
                glava_2 = Label(image=galaxy_icon,bg='#3B4EA3',cursor='hand1')
                glava_2.image = galaxy_icon
                glava_2.place(relx=0.7,rely=0.4,anchor=CENTER)
                glava_2.bind('<Button-1>',main_galaxy)

                path_to_choose_label = os.path.abspath('media/screen_resolution/1920_1080/main_menu/glavy/choose.png')
                choose_icon = PhotoImage(file=path_to_choose_label)
                choose_label = Label(image=choose_icon,bg='#3B4EA3')
                choose_label.image = choose_icon
                choose_label.place(relx=0.3,rely=0.1)

            path_to_coin = os.path.abspath('media/screen_resolution/1920_1080/main_menu/coin.png')
            coin_icon = PhotoImage(file = path_to_coin)
            coin_icon_spawn = Label(image=coin_icon,bg='#3B4EA3')
            coin_icon_spawn.grid(row=0,column=0)

            coins_label = Label(text =coins, fg = "#E6B71C",
              bg = "#3B4EA3",font = ("Inpact", 39,'bold'))
            coins_label.grid(row=0,column=1)
            print(w,h)
            root.geometry("{}x{}".format(w,h))
            root.title('Iok Jump')
            
            path_character = os.path.abspath('media/screen_resolution/1920_1080/main_menu/ball.png')
            character = PhotoImage(file=path_character)
            for_menu = Label(image=character,bg='#3B4EA3')
            for_menu.grid(row=5,column=2)

            path_to_welcome = os.path.abspath('media/screen_resolution/1920_1080/main_menu/welcome.png')
            welcome = PhotoImage(file=path_to_welcome)
            label = Label(root, image=welcome,bg='#3B4EA3')
            label.place(relx=0.5,rely=0.1, anchor=CENTER)

            path_to_icon_start_button = os.path.abspath('media/screen_resolution/1920_1080/main_menu/start_button.png')
            icon_start_button = PhotoImage(file=path_to_icon_start_button)
            button = Label(root,image=icon_start_button,cursor='hand1',width=315,height=140,bg='#3B4EA3')
            button.bind('<Button-1>',glavy)#main
            button.place(relx=0.5,rely=0.3,anchor=CENTER)

            path_to_icon_shop_button = os.path.abspath('media/screen_resolution/1920_1080/main_menu/shop_button.png')
            icon_shop_button = PhotoImage(file=path_to_icon_shop_button)
            button_shop = Label(root, image=icon_shop_button, cursor='hand1',width=315,height=140,bg='#3b4ea3')
            button_shop.bind('<Button-1>',shop_ui)
            button_shop.place(relx=0.5,rely=0.5,anchor=CENTER)

            path_to_icon_exit_button = os.path.abspath('media/screen_resolution/1920_1080/main_menu/exit_button.png')
            icon_exit_button = PhotoImage(file=path_to_icon_exit_button)
            button_exit = Label(root,image=icon_exit_button,cursor='hand1',width=315,height=140,bg='#3B4EA3')
            button_exit.bind('<Button-1>',exit)
            button_exit.place(relx=0.5,rely=0.7,anchor=CENTER)

            volume_icon()

            root.config(bg='#3B4EA3')

            root.bind('<Return>',glavy)
            root.mainloop()

        elif w == 1366 or 1360 and h == 768:
            def glavy(event):
                remove_all()

                path_to_button_home = os.path.abspath('media/game_icons/home.png')
                button_home_lbl_icon = PhotoImage(file=path_to_button_home)
                button_home_lbl_icon.image = button_home_lbl_icon
                button_home_lbl = Label(root,image=button_home_lbl_icon,cursor='hand1',bg='#3B4EA3')
                button_home_lbl.place(relx=0.90,rely=0.04,anchor=CENTER)
                button_home_lbl.bind('<Button-1>',back_home)

                #sky glava
                path_to_sky_icon = os.path.abspath('media/screen_resolution/1366_768/main_menu/glavy/sky_glava/sky.png')
                sky_icon = PhotoImage(file=path_to_sky_icon)
                glava_1 = Label(image=sky_icon,bg='#3B4EA3',cursor='hand1')
                glava_1.image = sky_icon
                glava_1.place(relx=0.5,rely=0.4,anchor=CENTER)
                glava_1.bind('<Button-1>', main_sky)
                
                #galaxy glava 
                path_to_galaxy_icon = os.path.abspath('media/screen_resolution/1366_768/main_menu/glavy/galaxy_glava/galaxy.png')
                galaxy_icon = PhotoImage(file=path_to_galaxy_icon)
                glava_2 = Label(image=galaxy_icon,bg='#3B4EA3',cursor='hand1')
                glava_2.image = galaxy_icon
                glava_2.place(relx=0.7,rely=0.4,anchor=CENTER)
                glava_2.bind('<Button-1>', main_galaxy)


                path_to_choose_label = os.path.abspath('media/screen_resolution/1366_768/main_menu/glavy/choose.png')
                choose_icon = PhotoImage(file=path_to_choose_label)
                choose_label = Label(image=choose_icon,bg='#3B4EA3')
                choose_label.image = choose_icon
                choose_label.place(relx=0.4,rely=0.2)
          #  print(w,h)
            root.geometry("{}x{}".format(w,h))
            root.title('Iok Jump')
            
            path_to_coin = os.path.abspath('media/screen_resolution/1366_768/main_menu/coin.png')
            coin_icon = PhotoImage(file = path_to_coin)
            coin_icon_spawn = Label(image=coin_icon,bg='#3B4EA3')
            coin_icon_spawn.grid(row=0,column=0)

            coins_label = Label(text =coins, fg = "#E6B71C",
            bg = "#3B4EA3",font = ("Inpact", 25,'bold'))
            coins_label.grid(row=0,column=2)

            path_to_welcome = os.path.abspath('media/screen_resolution/1366_768/main_menu/welcome.png')
            welcome = PhotoImage(file=path_to_welcome)
            label = Label(root, image=welcome,bg='#3B4EA3')
            label.place(relx=0.5,rely=0.1, anchor=CENTER)

            path_character = os.path.abspath('media/screen_resolution/1366_768/main_menu/ball.png')
            character = PhotoImage(file=path_character)
            for_menu = Label(image=character,bg='#3B4EA3')
            for_menu.grid(row=6,column=3)

            path_to_icon_start_button = os.path.abspath('media/screen_resolution/1366_768/main_menu/start_button.png')
            icon_start_button = PhotoImage(file=path_to_icon_start_button)
            button = Label(root,image=icon_start_button,cursor='hand1',width=315,height=140,bg='#3B4EA3')
            button.bind('<Button-1>',glavy) #glavy
            button.place(relx=0.5,rely=0.3,anchor=CENTER)

            path_to_icon_shop_button = os.path.abspath('media/screen_resolution/1366_768/main_menu/shop_button.png')
            icon_shop_button = PhotoImage(file=path_to_icon_shop_button)
            button_shop = Label(root, image=icon_shop_button, cursor='hand1',width=315,height=140,bg='#3b4ea3')
            button_shop.bind('<Button-1>',shop_ui)
            button_shop.place(relx=0.5,rely=0.5,anchor=CENTER)

            volume_icon()

            path_to_icon_exit_button = os.path.abspath('media/screen_resolution/1366_768/main_menu/exit_button.png')
            icon_exit_button = PhotoImage(file=path_to_icon_exit_button)
            button_exit = Label(root,image=icon_exit_button,cursor='hand1',width=315,height=140,bg='#3B4EA3')
            button_exit.bind('<Button-1>',exit)
            button_exit.place(relx=0.5,rely=0.7,anchor=CENTER)

            root.config(bg='#3B4EA3')


            root.bind('<Return>',glavy)
            root.mainloop()
    def remove_all():

        try:
            choose_label.destroy()
            glava_1.destroy()
            glava_2.destroy()

        except:
            print('Shittt')
        try:
            button.destroy()
            button_shop.destroy()
            button_exit.destroy()
            label.destroy()
            button_home_lbl.destroy()
            frame.destroy()
            samolet1.destroy()
            samolet2.destroy()
            samolet3.destroy()
            samolet4.destroy()
            samolet5.destroy()
            samolet6.destroy()
            samolet7.destroy()
            samolet8.destroy()
            samolet9.destroy()
            samolet10.destroy()
            samolet11.destroy()
            samolet12.destroy()
            button_cina.destroy()
        except:
            print('Something went wrong.')
    def back_home(event):
        remove_all()
        main_window()
    def shop_ui(event): 
        global button_home_lbl
        global samolet1 
        global samolet2 
        global samolet3 
        global samolet4 
        global samolet5 
        global samolet6 
        global samolet7 
        global samolet8
        global samolet9
        global samolet10 
        global samolet11 
        global samolet12 
        global frame

        try:
            remove_all()
        except:
            None

        path_to_button_home = os.path.abspath('media/game_icons/home.png')
        button_home_lbl_icon = PhotoImage(file=path_to_button_home)
        button_home_lbl_icon.image = button_home_lbl_icon
        button_home_lbl = Label(root,image=button_home_lbl_icon,cursor='hand1',bg='#3B4EA3')
        button_home_lbl.place(relx=0.90,rely=0.04,anchor=CENTER)
        button_home_lbl.bind('<Button-1>',back_home)

        images_path = [os.path.abspath('media/game_icons/characters/airplanes/1.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/2.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/3.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/4.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/5.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/6.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/7.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/8.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/9.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/10.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/11.png'),
                       os.path.abspath('media/game_icons/characters/airplanes/12.png'),
        ]
        image1 = PhotoImage(file=images_path[0])
        image2 = PhotoImage(file=images_path[1])
        image3 = PhotoImage(file=images_path[2])
        image4 = PhotoImage(file=images_path[3])
        image5 = PhotoImage(file=images_path[4])
        image6 = PhotoImage(file=images_path[5])
        image7 = PhotoImage(file=images_path[6])
        image8 = PhotoImage(file=images_path[7])
        image9 = PhotoImage(file=images_path[8])
        image10 = PhotoImage(file=images_path[10])
        image11 = PhotoImage(file=images_path[9])
        image12 = PhotoImage(file=images_path[11])

        image1.image=image1
        image2.image = image2
        image3.image = image3 
        image4.image = image4 
        image5.image = image5 
        image6.image = image6 
        image7.image = image7
        image8.image = image8 
        image9.image = image9 
        image10.image = image10
        image11.image = image11 
        image12.image = image12 

        path_to_cina_btn = os.path.abspath('media/screen_resolution/1920_1080/main_menu/cina_button.png')
        cina_btn_icon = PhotoImage(file=path_to_cina_btn)
        cina_btn_icon.image = cina_btn_icon

        frame = Frame(width=700,height=700,bg='#5D2EAB')
        frame.place(relx=0.4,rely=0.25)

        ####################################
        def un():
            try:
                samolet1.config(bg='#5D2EAB')
                samolet2.config(bg='#5D2EAB')
                samolet3.config(bg='#5D2EAB')
                samolet4.config(bg='#5D2EAB')
                samolet5.config(bg='#5D2EAB')
                samolet6.config(bg='#5D2EAB')
                samolet7.config(bg='#5D2EAB')
                samolet8.config(bg='#5D2EAB')
                samolet9.config(bg='#5D2EAB')
                samolet10.config(bg='#5D2EAB')
                samolet11.config(bg='#5D2EAB')
                samolet12.config(bg='#5D2EAB')
            except:
                print('Something went wrong')
        #cina_slovar = {
         #   samolet1:'Default',
          #  samolet2:'150',
           # samolet3:'300',
            #samolet4:'450',
       #     samolet5:'600',
        #    samolet6:'750',
         #   samolet7:'850',
          #  samolet8:'900',
           # samolet9:'1000',
       #     samolet10:'1250',
        #    samolet11:'1500',
         #   samolet12:'2000'
        #}
        def sam1(event):
            global button_cina
            un()
            samolet1.config(bg='#7B24AE')
            button_cina = Label(image=cina_btn_icon,bg='#3B4EA3',text='Enabled',font=('Android Assassin',40),fg='white',compound= tk.CENTER)
            button_cina.place(relx=0.6,rely=0.7)
        samolet1 = Label(frame,image=image1,bg='#5D2EAB',cursor='hand1')
        samolet1.grid(row=0,column=0)
        samolet1.bind('<Button-1>', sam1)

        def sam2(event):
            un()
            samolet2.config(bg='#7B24AE')
        samolet2 = Label(frame,image=image2,bg='#5D2EAB',cursor='hand1',width=200)
        samolet2.grid(row=0,column=1)
        samolet2.bind('<Button-1>',sam2)

        def sam3(event):
            un()
            samolet3.config(bg='#7B24AE')
        samolet3 = Label(frame,image=image3,bg='#5D2EAB',cursor='hand1')
        samolet3.grid(row=0,column=2)
        samolet3.bind('<Button-1>', sam3)

        def sam4(event):
            un()
            samolet4.config(bg='#7B24AE')
        samolet4 = Label(frame,image=image4,bg='#5D2EAB',cursor='hand1',width=200)
        samolet4.grid(row=0,column=3)
        samolet4.bind('<Button-1>',sam4)

        def sam5(event):
            un()
            samolet5.config(bg='#7B24AE')
        samolet5 = Label(frame,image=image5,bg='#5D2EAB',cursor='hand1')
        samolet5.grid(row=0,column=4)
        samolet5.bind('<Button-1>',sam5)
######################################################
        def sam6(event):
            un()
            samolet6.config(bg='#7B24AE')
        samolet6 = Label(frame, image=image6,bg='#5D2EAB',cursor='hand1',width=200)
        samolet6.grid(row=1,column=0)
        samolet6.bind('<Button-1>',sam6)

        def sam7(event):
            un()
            samolet7.config(bg='#7B24AE')
        samolet7 = Label(frame, image=image7,bg='#5D2EAB',cursor='hand1')
        samolet7.grid(row=1,column=1)
        samolet7.bind('<Button-1>',sam7)

        def sam8(event):
            un()
            samolet8.config(bg='#7B24AE')
        samolet8 = Label(frame,image=image8,bg='#5D2EAB',cursor='hand1',width=200)
        samolet8.grid(row=1,column=2)
        samolet8.bind('<Button-1>',sam8)

        def sam9(event):
            un()
            samolet9.config(bg='#7B24AE')
        samolet9 = Label(frame,image=image9,bg='#5D2EAB',cursor='hand1')
        samolet9.grid(row=1,column=3)
        samolet9.bind('<Button-1>',sam9)

        def sam10(event):
            un()
            samolet10.config(bg='#7B24AE')
        samolet10 = Label(frame,image=image10,bg='#5D2EAB',cursor='hand1',width=200)
        samolet10.grid(row=1,column=4)
        samolet10.bind('<Button-1>',sam10)
#####################################################
        def sam11(event):
            un()
            samolet11.config(bg='#7B24AE')
        samolet11 = Label(frame,image=image11,bg='#5D2EAB',cursor='hand1')
        samolet11.grid(row=2,column=0)
        samolet11.bind('<Button-1>',sam11)

        def sam12(event):
            un()
            samolet12.config(bg='#7B24AE')
        samolet12 = Label(frame,image=image12,bg='#5D2EAB',cursor='hand1',width=200)
        samolet12.grid(row=2,column=1)
        samolet12.bind('<Button-1>',sam12)

        #scrollbar2 = Scrollbar(orient='vertical')
        #scrollbar2.config(command=text2.yview)
        #scrollbar2.pack('left',fill='y')
        #text2.config(yscrollcommand=scrollbar2.set)

    main_window()

window()

def exit():
    os.kill(os.getpid(),signal.SIGKILL())

###############################--THE--END--#########################################