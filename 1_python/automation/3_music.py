#!/bin/env python3

---
import os
def play(file):
    os.system("ffplay %s" %(file))
play("video1.mp4")


---
# 使用本地播放器
import os
app = ""
file = ""
os.system('app %s' %file)


---
# pygame 模块播放应约
# apt install portaudio19-dev
# pip install pygame
import time
import pygame
file = "file.mp3"

pygame.mixer.init()                     # 初始化
track = pygame.mixer.music.load(file)   # 加载音乐
pygame.mixer.music.play()               # 播放
time.sleep(10)
#pygame.mixer.music.pause()              # 暂停播放
pygame.mixer.music.stop()               # 停止播放



