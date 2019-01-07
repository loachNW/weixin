from urllib import request
import lxml
import lxml.html
import re
import json
import urllib.parse
from lxml import etree
import requests
import cssselect
import json,xlwt
import pyaudio
import wave
import sys
import wave
from pyaudio import PyAudio,paInt16
import base64
import os
import requests
import time
import itchat
from wxpy import *
import collections
import hashlib
import logging
from wxpy.api.messages import Message
from wxpy.ext.talk_bot_utils import get_context_user_id, next_topic
from wxpy.utils.misc import get_text_without_at_bot
from wxpy.utils import enhance_connection
from wxpy.compatible import *

bot = Bot(cache_path= 'Ture')# 生成缓存文件wxpy.pkl后，为该文件路径
tuling = Tuling(api_key='9d90c7fa414d4ae49362b99cfecedf4f')
print('机器人已经启动')# 我的小号，测试需谨慎
my_friednd = bot.groups().search('愿老蔡明天找个女朋友')# 如果想对所有好友实现机器人回复把参数my_friend改成chats = [Friend]# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friednd)
def reply_my_friednd(msg):
    tuling.do_reply(msg)# 进入交互式的 Python 命令行界面，并堵塞当前线程
embed()



# # 登录缓存路径,第一次设置为True
# os.chdir('C:/Users/ASUS/Desktop/')
# bot = Bot(cache_path= 'None')# 生成缓存文件wxpy.pkl后，为该文件路径
# tuling = Tuling(api_key='9d90c7fa414d4ae49362b99cfecedf4f')
# print('机器人已经启动')# 我的小号，测试需谨慎
# #chats = [Friend]
# my_friend = bot.groups().search('一生女子月月友')
# # 发送消息# 如果想对所有好友实现机器人回复把参数my_friend改成chats = [Friend]# 使用图灵机器人自动与指定好友聊天
# @bot.register(my_friend)
# def reply_my_friednd(msg):
#     if isinstance(msg.chat, Group) and not msg.is_at:#不@不回复
#         return
#     else:
#         tuling.do_reply(msg)# 进入交互式的 Python 命令行界面，并堵塞当前线程
# embed()