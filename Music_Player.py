import os,sys
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import threading
import pygame
import random

def play():
    if len(res):
        pygame.mixer.init()
        global num,list_box
        while playing:
            if not pygame.mixer.music.get_busy():
                netxMusic = res[num]
                list_box.selection_clear(list_box.curselection())
                list_box.select_set(num)
                pygame.mixer.music.load(netxMusic)
                pygame.mixer.music.play(1)
                netxMusic = netxMusic.split('/')[-1]
                musicName.set('Playing...' + netxMusic)
            else:
                time.sleep(0.5)
            try:
                if not pygame.mixer.music.get_busy():
                    num=get_next(number=num)
                else:
                    pass
            except:
                break

def buttonPlayClick():
    global pause_resume,buttonPlay,buttonNext,buttonPrev,playing,t
    buttonNext['state'] = 'normal'
    buttonPrev['state'] = 'normal'
    buttonPattern['state']='normal'
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
        playing=True
        pygame.mixer.music.unpause()
        pause_resume.set('PAUSE')

def buttonStopClick():
    # global playing
    # playing = False
    pygame.mixer.music.stop()

def buttonNextClick(event=Event()):
    buttonNext['state']='disabled'
    global playing,t
    playing = False
    pygame.mixer.music.stop()
    global num,res
    num=(num+1)%len(res)
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

def buttonPrevClick(event=Event()):
    global playing,t
    playing = False
    pygame.mixer.music.stop()
    global num,res
    num=(len(res)+num-1)%len(res)
    playing = True
    t = threading.Thread(target=play)
    t.start()

def buttonPatternClick(event=Event())->None:
    global pattern,patternName
    pattern='rand' if pattern=='order' else 'circle' if pattern=='rand' else 'order'
    patternName.set(pattern)
    return

def select_directory(event=Event()):
    # Open a file dialog to select the music directory
    global folder,res,list_box
    folder = filedialog.askdirectory() if folder=='' else folder
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
    folder=''
    if len(res) == 0:
        messagebox.showwarning("Warning", "No music files found in the selected directory!")
    else:
        # Loop through the music list and add each item to the listbox
        for song in res:
            list_box.insert(END, song.split('/')[-1])
        global playing
        playing = True
        # 根据情况禁用和启用相应的按钮
        buttonPlay['state'] = 'normal'
        buttonStop['state'] = 'normal'
        # buttonPause['state'] = 'normal'
        pause_resume.set('PLAY')
        list_box.select_set(num)

def get_next(number:int)->int:
    global num,pattern,res
    length=len(res)
    num=(number+1)%length if pattern=='order' else random.randint(a=0,b=length-1) if pattern=='rand' else number
    return num

def play_song(event=Event()):
    pause_resume.set("PLAY")
    global num,playing,list_box
    current_song_index = list_box.curselection()[0]
    num=current_song_index
    pygame.mixer.music.stop()
    buttonPlayClick()
    return

def main():
    global folder
    if len(sys.argv)>1:
        path=sys.argv[1]
        if os.path.isdir(path):
            folder=path
        else:
            if path.endswith('.mp3'):
                res.append(path)
            else:
                pass
    else:
        pass

if __name__=="__main__":

    global folder,res,num,pattern
    folder =''
    res = []
    num = 0
    pattern='order'

    main()

    pygame.init()

    root = tkinter.Tk()
    root.title('Music Player')
    # root.iconbitmap('pic.ico')
    root.geometry('400x500+600+100')
    root.resizable(True,True)

    list_box = Listbox(root)
    list_box.pack(fill=BOTH, expand=1)
    list_box.bind('<Double-Button-1>', play_song)
    list_box.bind('<Return>',play_song)

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
    buttonPrev = Button(root, text='◀',command=buttonPrevClick,width=5,bg="lightgreen")
    buttonPrev['state'] = 'disabled'

    # 播放模式
    patternName=StringVar(root,value=pattern)
    buttonPattern=Button(root, textvariable=patternName, command=buttonPatternClick,width=5,bg='white')
    buttonPattern['state']='disabled'

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
    buttonPattern.pack(padx=4,pady=5,side=LEFT,expand=True)
    select_button.pack(padx=4,pady=5,side=TOP)

    root.bind('<KeyPress-Left>',buttonPrevClick)
    root.bind('<KeyPress-Right>',buttonNextClick)
    root.bind('<Control-Return>',select_directory)
    root.bind('<Shift-Return>',buttonPatternClick)

    # 显示
    root.mainloop()
    pass