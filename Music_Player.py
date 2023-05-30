import os
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import threading
import pygame

def play():
    if len(res):
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                netxMusic = res[num]
                pygame.mixer.music.load(netxMusic)
                pygame.mixer.music.play(1)
                if len(res) -1 == num:
                    num = 0
                else:
                    num = num + 1
                netxMusic = netxMusic.split('/')[-1]
                musicName.set('Playing...' + netxMusic)
            else:
                time.sleep(0.5)

def buttonPlayClick():
    global pause_resume,buttonPlay,buttonNext,buttonPrev,playing,t
    buttonNext['state'] = 'normal'
    buttonPrev['state'] = 'normal'
    # 选择要播放的音乐文件夹
    if pause_resume.get() == 'PLAY':
        pause_resume.set('PAUSE')
        playing = True
        # 创建一个线程来播放音乐，当前主线程用来接收用户操作
        t = threading.Thread(target=play)
        t.start()
    elif pause_resume.get() == 'PAUSE':
        # pygame.mixer.init()
        playing=False
        pygame.mixer.music.pause()
        pause_resume.set('CONTINUE')
    elif pause_resume.get() == 'CONTINUE':
        # pygame.mixer.init()
        pygame.mixer.music.unpause()
        pause_resume.set('PAUSE')
        playing=True

def buttonStopClick():
    global playing
    playing = False
    pygame.mixer.music.stop()

def buttonNextClick():
    buttonNext['state']='disabled'
    global playing
    playing = False
    pygame.mixer.music.stop()
    global num
    if len(res) == num:
        num = 0
    playing = True
    # 创建线程播放音乐,主线程用来接收用户操作
    t = threading.Thread(target=play)
    t.start()
    buttonNext['state']='normal'

def closeWindow():
    global playing
    playing = False
    time.sleep(0.3)
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy()

def buttonPrevClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    global num
    if num == 0:
        num = len(res) - 2
    else:
        num -= 2
    playing = True
    t = threading.Thread(target=play)
    t.start()

def select_directory():
    # Open a file dialog to select the music directory
    global folder,res
    folder = filedialog.askdirectory()
    # Clear the listbox
    list_box.delete(0, END)
    # Create an empty list to store the names of the music files
    music_list = []
    # Walk through the music folder and add the names of music files to the list
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav'):
                music_list.append(file)
    for i in music_list:
            res.append(folder+"/"+i)
    if len(music_list) == 0:
        messagebox.showwarning("Warning", "No music files found in the selected directory!")
    else:
        # Loop through the music list and add each item to the listbox
        for song in music_list:
            list_box.insert(END, song)
        global playing
        playing = True
        # 根据情况禁用和启用相应的按钮
        buttonPlay['state'] = 'normal'
        buttonStop['state'] = 'normal'
        # buttonPause['state'] = 'normal'
        pause_resume.set('PLAY')

def play_song(event):
    pause_resume.set("PLAY")
    global num,playing
    current_song_index = list_box.curselection()[0]
    # Get the name of the selected song
    current_song_name = list_box.get(current_song_index)
    musicName.set('Playing...' + current_song_name)
    # Construct the path to the selected song
    current_song_path = os.path.join(folder, current_song_name)
    # Stop any currently playing music
    pygame.mixer.music.stop()
    # Load and play the selected song
    pygame.mixer.music.load(current_song_path)
    pygame.mixer.music.play()
    num=current_song_index+1
    buttonPlayClick()

pygame.init()

root = tkinter.Tk()
root.title('Music Player')
root.geometry('400x500+600+100')
root.resizable(True,True)

list_box = Listbox(root)
list_box.pack(fill=BOTH, expand=1)
list_box.bind('<Double-Button-1>', play_song)

global folder,res,num
folder =''
res = []
num = 0

# 窗口关闭
root.protocol('WM_DELETE_WINDOW', closeWindow)

# 播放按钮
global pause_resume,buttonPlay
pause_resume = StringVar(root,value='PLAY')
buttonPlay = Button(root,textvariable=pause_resume,command=buttonPlayClick,width=15,bg="lightblue",font="Times 10 bold")
buttonPlay['state'] = 'disabled'

# 停止按钮
buttonStop = Button(root, text='STOP',command=buttonStopClick,width=20,bg="red",font="Times 10 bold")
buttonStop['state'] = 'disabled'

# 下一首
buttonNext = Button(root, text='▶',command=buttonNextClick,width=5,bg="yellow")
buttonNext['state'] = 'disabled'
# 上一首
buttonPrev = Button(root, text='◀',command=buttonPrevClick,width=5,bg="lightgreen",font="Times 10 bold")
buttonPrev['state'] = 'disabled'

# 标签
musicName = StringVar(root, value='NONE')
labelName = Label(root, textvariable=musicName,width=50,bg="grey",font="Times 10 bold")

# Create a button to select a music directory
select_button = Button(root, text='Select Directory', command=select_directory,width=20,bg="white",font="Times 10 bold")

#布局
labelName.pack(fill=X)
buttonPrev.pack(padx=4,pady=5,side=LEFT,expand=True)
buttonPlay.pack(padx=4,pady=5,side=LEFT,expand=True)
buttonNext.pack(padx=4,pady=5,side=LEFT,expand=True)
buttonStop.pack(padx=4,pady=5,side=TOP)
select_button.pack(padx=4,pady=5,side=TOP)

# 显示
root.mainloop()