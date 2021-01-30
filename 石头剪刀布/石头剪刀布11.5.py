#石头剪刀布11.5.py
import pygame
import sys
import time
import random
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import PySimpleGUI as sg
import time
import pyglet
#进度条
items = range(100)
for i, item in enumerate(items):
  sg.one_line_progress_meter('这是一个进度条', i+1, len(items), '-key-')
  time.sleep(0.0001)


live = 0
pygame.init()
screen = pygame.display.set_mode([800, 450])
# 设置标题
pygame.display.set_caption("人机对战石头剪刀布娱乐软件10.5")
# 加载图标
image = pygame.image.load("图片/game.jpg")
pygame.display.set_icon(image)

# r tm
print('淇淇')
#绘制函数


# 加载图片
黑色 = pygame.image.load('图片/黑色.png')
黑色2 = pygame.image.load('图片/黑色2.png')
背景 = pygame.image.load('图片/背景.jpg')
电脑 = pygame.image.load('图片/电脑.png')
你 = pygame.image.load('图片/你.png')
剪刀 = pygame.image.load('图片/剪刀.png')
布 = pygame.image.load('图片/布.png')
石头 = pygame.image.load('图片/石头.png')
胜 = pygame.image.load('图片/胜.png')
败 = pygame.image.load('图片/败.png')
提示 = pygame.image.load('图片/提示.png')
平局 = pygame.image.load('图片/平局.png')
再见 = pygame.image.load('图片/再见.png')
石头剪刀布 = pygame.image.load('图片/石头剪刀布.png')
开始 = pygame.image.load('图片/10.0.png')
分数 = pygame.image.load('图片/分数.png')
# 画出来

screen.blit(石头剪刀布, [50, 80])
pygame.display.update()
time.sleep(1.5)
screen.blit(黑色, [80, 80])
pygame.display.update()
screen.blit(黑色2, [0, 101])
pygame.display.update()
time.sleep(1.5)
screen.blit(开始, [50, 80])
pygame.display.update()
time.sleep(1.5)
screen.blit(背景, [0, 0])
pygame.display.update()
screen.blit(电脑, [0, 0])
pygame.display.update()
screen.blit(你, [700, 0])
pygame.display.update()
screen.blit(提示, [275, 407])
pygame.display.update()
print('a 石头 s 剪刀 d布 f退出')
MUSIC = 27
# 启动定时器，设置时间间隔
pygame.time.set_timer(MUSIC, 248400)
def main():
    # 音乐的路径
    file = r'C418 - Minecraft.mp3'
    # 初始化
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(file)
    # 开始播放音乐
    pygame.mixer.music.play()
#-------------------------------------------------
main()
def draw():
    #  创建字体对象 ------------------
    font = pygame.font.SysFont('SimHei', 20)
    # 创建文本对象 ------------------
    content = font.render('分数：' + str(live), True, [255, 255, 255])
    # 绘制文本 ------------------
    screen.blit(content, [680,364])

#----------------------------------------------------
#-------------------------------
while True:
    draw()
    pygame.display.update()
    # '循环遍历事件列表
    for event in pygame.event.get():
        # 判断退出事件
        if event.type == pygame.QUIT:
            # 停止运行
            sys.exit()
        elif event.type == MUSIC:
            main()
        elif event.type == pygame.KEYDOWN:
            # 如果按下A键
            if event.key == pygame.K_a:

                screen.blit(石头, [700, 300])
                pygame.display.set_caption("石头")
                image = pygame.image.load("图片/game2.jpg")
                pygame.display.set_icon(image)
                pygame.display.update()
                time.sleep(1)
                num = random.randint(1, 3)
                if num == 1:
                    screen.blit(石头, [0, 300])
                    pygame.display.set_caption("石头")
                    image = pygame.image.load("图片/game2.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('平局')
                    screen.blit(平局, [640, 360])
                    pygame.display.update()
                elif num == 2:
                    screen.blit(剪刀, [0, 300])
                    pygame.display.set_caption("剪刀")
                    image = pygame.image.load("图片/game3.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('玩家赢')
                    screen.blit(胜, [640, 360])
                    pygame.display.update()
                    live = live + 1
                    liva = str(live)
                    print('分数' + liva)
                    f = open('分数.txt', 'a')
                    f.write('分数' + liva + '\n')
                    f.close()
                elif num == 3:
                    screen.blit(布, [0, 300])
                    pygame.display.set_caption("布")
                    image = pygame.image.load("图片/game4.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('玩家输')
                    screen.blit(败, [640, 360])
                    pygame.display.update()
                    live = live - 1
                    livb = str(live)
                    print('分数' + livb)
                    f = open('分数.txt', 'a')
                    f.write('-----------------------''\n')
                    f.close()
                    print('分数-1')
                    pass
                    # 如果按下s
            elif event.key == pygame.K_s:
                screen.blit(剪刀, [700, 300])
                pygame.display.set_caption("剪刀")
                image = pygame.image.load("图片/game3.jpg")
                pygame.display.set_icon(image)
                pygame.display.update()
                time.sleep(1)
                num = random.randint(1, 3)
                if num == 1:
                    screen.blit(石头, [0, 300])
                    pygame.display.set_caption("石头")
                    image = pygame.image.load("图片/game2.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('玩家输')
                    screen.blit(败, [640, 360])
                    pygame.display.update()
                    live = live - 1
                    livb = str(live)
                    print('分数' + livb)
                    f = open('分数.txt', 'a')
                    f.write('-----------------------''\n')
                    f.close()
                    print('分数-1')
                    pass
                elif num == 2:
                    screen.blit(剪刀, [0, 300])
                    pygame.display.set_caption("剪刀")
                    image = pygame.image.load("图片/game3.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('平局')
                    screen.blit(平局, [640, 360])
                    pygame.display.update()
                elif num == 3:
                    screen.blit(布, [0, 300])
                pygame.display.set_caption("布")
                image = pygame.image.load("图片/game4.jpg")
                pygame.display.set_icon(image)
                pygame.display.update()
                print('玩家赢')
                screen.blit(胜, [640, 360])
                pygame.display.update()
                live = live + 1
                liva = str(live)
                print('分数' + liva)
                f = open('分数.txt', 'a')
                f.write('分数' + liva + '\n')
                f.close()
                # 如果按下d
            elif event.key == pygame.K_d:
                screen.blit(布, [700, 300])
                pygame.display.set_caption("布")
                image = pygame.image.load("图片/game4.jpg")
                pygame.display.set_icon(image)
                pygame.display.update()
                time.sleep(1)
                num = random.randint(1, 3)
                if num == 1:
                    screen.blit(石头, [0, 300])
                    pygame.display.set_caption("石头")
                    image = pygame.image.load("图片/game2.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('玩家赢')
                    screen.blit(胜, [640, 360])
                    pygame.display.update()
                    live = live + 1
                    liva = str(live)
                    print('分数' + liva)
                    f = open('分数.txt', 'a')
                    f.write('分数' + liva + '\n')
                    f.close()
                elif num == 2:
                    screen.blit(剪刀, [0, 300])
                    pygame.display.set_caption("剪刀")
                    image = pygame.image.load("图片/game3.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('玩家输')
                    screen.blit(败, [640, 360])
                    pygame.display.update()
                    live = live - 1
                    livb = str(live)
                    print('分数' + livb)
                    f = open('分数.txt', 'a')
                    f.write('-----------------------''\n')
                    f.close()
                    print('分数-1')
                    pass
                elif num == 3:
                    screen.blit(布, [0, 300])
                    pygame.display.set_caption("布")
                    image = pygame.image.load("图片/game4.jpg")
                    pygame.display.set_icon(image)
                    pygame.display.update()
                    print('平局')
                    screen.blit(平局, [640, 360])
                    pygame.display.update()
            elif event.key == pygame.K_f:
                print('再见ヾ(￣▽￣)Bye~Bye~')
                screen.blit(再见, [250, 80])
                pygame.display.update()
                time.sleep(2)
                sys.exit(0)
            #版本查询
            elif event.key == pygame.K_F1:
                tkinter.messagebox.showinfo('成就', '获得成就：乱按键盘')
                tkinter.messagebox.showinfo(title='版本查询', message='版本号：10.5''\n' '作者：沈子淇''\n''开发日期：2020.1')
            elif event.key == pygame.K_t:
                tkinter.messagebox.showinfo('成就', '获得成就：输入指令')
            elif event.key == pygame.K_ESCAPE:
                tkinter.messagebox.showinfo('成就', '获得成就：你的Esc键坏掉了')
            elif event.key == pygame.K_F5:
                tkinter.messagebox.showinfo('？？？', '这是一个能帮你自动打游戏的程序')
                tkinter.messagebox.showinfo('？？？', '可用次数：1')
                tkinter.messagebox.showinfo('？？？', '自动挂机打游戏中……')
                tkinter.messagebox.showinfo('？？？', 'FBB!open the door!')
            #彩蛋程序
            elif event.key == pygame.K_b:
                # !/usr/bin/env python
                # -*- coding:utf-8 -*-
                from tkinter import *

                tkinter.messagebox.showinfo('成就', '获得成就：彩蛋探索者')
                tkinter.messagebox.showinfo('彩蛋', 'Loading...')
                time.sleep(1)
                tkinter.messagebox.showinfo('彩蛋', '正确')
                tkinter.messagebox.showinfo('彩蛋', 'name：' + '用户''彩蛋平台欢迎您！')
                f = open('分数.txt', 'a')
                f.write('分数：100000''\n')
                f.close()
                tkinter.messagebox.showinfo('提示', '分数写入成功，共写入100000分')
