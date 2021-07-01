import cv2
import screen_brightness_control as sbc
import time
import os
from tkinter import *
import threading
import tkinter as tk

os.path.exists('C:\Brightness')
if not os.path.exists('C:\Brightness'):
    os.mkdir('C:\Brightness')
값=1
출력=5
def on():
    global 출력
    btn1['state']=tk.DISABLED
    while 값==1:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 노트북 웹캠을 카메라로 사용2
        cap.set(3, 1280)  # 너비
        cap.set(4, 10)  # 높이

        ret, frame = cap.read()  # 사진 촬영
        #cv2.imwrite(os.path.join(path, 'collect image.png'), frame) #만든 경로에 사진 저장
        cv2.imwrite('C:\Brightness\collect image.png', frame)  # 사진 저장


        from PIL import Image

        img = Image.open('C:\Brightness\collect image.png') #찍은 사진 불러오기


        img_size = img.size
        img = img.resize((50, 20)) #50*20으로 리사이즈
        img_size = img.size

        imgGray = img.convert('L') #흑백처리
        #imgGray.save('C:\Brightness\Test_gray.png') #흑백사진 저장

        pixels = list(imgGray.getdata())
        i=1
        dic={}  #딕셔너리 설정
        while i<=255:
            a=pixels.count(i)
            dic[i]=a
            i=i+1

        영단=0
        i=1
        while i<=55:
            U=dic[i]
            영단=영단+U
            i=i+1
        일단=0
        while 55<i<=75:
            U=dic[i]
            일단=일단+U
            i=i+1
        이단=0
        while 75<i<=95:
            U=dic[i]
            이단=이단+U
            i=i+1
        삼단=0
        while 95<i<=115:
            U=dic[i]
            삼단=삼단+U
            i=i+1

        사단=0
        while 115<i<=135:
            U=dic[i]
            사단=사단+U
            i=i+1
        오단=0
        while 135<i<=155:
            U=dic[i]
            오단=오단+U
            i=i+1
        육단=0
        while 155<i<=175:
            U=dic[i]
            육단=육단+U
            i=i+1
        칠단=0
        while 175<i<=195:
            U=dic[i]
            칠단=칠단+U
            i=i+1
        팔단=0
        while 195<i<=215:
            U=dic[i]
            팔단=팔단+U
            i=i+1
        구단=0
        while 215<i<=235:
            U=dic[i]
            구단=구단+U
            i=i+1
        십단=0
        while 235<i<=255:
            U=dic[i]
            십단=십단+U
            i=i+1
        aa=[영단, 일단, 이단, 삼단, 사단, 오단, 육단, 칠단, 팔단, 구단, 십단]

        i=0
        while True:  #가장 높은 단수 찾기 (출력=단수)
            if max(aa)==aa[i]:
                출력=i
                break
            else:
                i=i+1

        if 출력==0:
            br=5
        elif 1<=출력<=7:
            br=출력*10+20

        else:
            br=100
        sbc.set_brightness(br)
        print(출력)
        time.sleep(1.5)


def th():
    loop=threading.Thread(target=on)
    loop.start()


def off():
    global 값
    값=0
    time.sleep(2.1)
    btn1['state']=tk.NORMAL
    값=1
    print('재시작 준비')


root=Tk()
root.title("화면밝기")
root.geometry("300x200")
root.resizable(False, False)

frame2 = tk.Frame(root, width=150, height=200, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

label1=Label(frame2, text="밝기를 자동 조절합니다.")
label1.pack()

btn1=Button(frame2, fg="red", width=10, height=5, text="On", command=th)
btn1.pack()

btn2 = Button(frame2, fg="red", width=10, height=5, text="Off", command=off)
btn2.pack()


root.mainloop()



