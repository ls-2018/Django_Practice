# coding: utf-8
import itchat
import tkinter.messagebox
# import winsound
import os


# import pygame
# 参考阅读https://mp.weixin.qq.com/s/60SYy9GLmrhO4KEtPPGLZg)

def alarm():
    # Windows嗡鸣声
    # winsound.Beep(1000, 3000)
    #     # Mac语音
    os.system('say "有人发红包了，赶紧去抢啊！红红火火恍恍惚惚哈哈哈哈"')
    # 播放MP3
    # pygame.mixer.init()
    # track = pygame.mixer.music.load('alarm.mp3')
    # pygame.mixer.music.play()
    # tkinter.messagebox.showinfo('重要提醒','有人发红包了！')


#
@itchat.msg_register('Note', isGroupChat=True)
def get_note(msg):
    if '红包' in msg['Text']:
        print('note:', msg['Text'])
        alarm()


# 注册消息响应事件，类型TEXT，文本消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def _(msg):
    print('text:', msg['Text'])


# 分享名片
@itchat.msg_register(itchat.content.ATTACHMENT)
def _(msg):
    msg['Text'](msg['Filename'])


itchat.auto_login(hotReload=True)
itchat.send('hello,file helper', toUserName='filehelper')   # 发送消息，
itchat.run()
itchat.logout()

'''
参数                 类型              Text建值
TEXT                文本               文本内容
MAP                 地图               位置文本   
CARD                名片               
SHARING             分享
PICTURE             图片、表情           下载
RECORDING           语音                下载
ATTACHMENT          附件                下载
VIDEO               小视频               下载
FRIENDS             好友邀请           添加参数
SYSTEM              系统消息
NOTE                通知

'''
