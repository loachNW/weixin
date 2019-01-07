from urllib import request
import lxml
import lxml.html
import re
import functools
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
import atexit
import functools
import logging
import os.path
import tempfile
from pprint import pformat
from threading import Thread

from wxpy.api.chats import Chat, Group, Member, User
from wxpy.compatible.utils import force_encoded_string_output
from wxpy.utils import wrap_user_name, repr_message
from wxpy.api.consts import ATTACHMENT, CARD, FRIENDS, MAP, PICTURE, RECORDING, SHARING, TEXT, VIDEO
from wxpy.compatible import *




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



'''
KEY = '9d90c7fa414d4ae49362b99cfecedf4f'
def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    print(msg)
    data = {
        'key'   : KEY,
        'info'   : msg,   #从好友哪儿接受到的消息
        'userid'  : 'wechat---rebot',  #这里随意写点什么都行
    }
    try:
        # 发送一个post请求
        r = requests.post(apiUrl, data =data).json()
        # 获取文本信息，若没有‘Text’ 值，将返回Nonoe
        return r.get('text')
    except:
        return ('没有返回信息')
# 通过定义装饰器加强函数 tuling_reply(msg) 功能，获取注册文本信息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 设置一个默认回复，在出现问题仍能正常回复信息
    defaultReply = 'I received: ' +msg['Text']
    reply = get_response(msg['Text'])
    # a or b 表示，如有a有内容，那么返回a，否则返回b
    return reply or defaultReply
# 使用热启动，不需要多次扫码
itchat.auto_login(hotReload=None)
itchat.run()




 # upload

[文档]    def upload_file(self, path):
        """
        | 上传文件，并获取 media_id
        | 可用于重复发送图片、表情、视频，和文件

        :param path: 文件路径
        :return: media_id
        :rtype: str
        """

        logger.info('{}: uploading file: {}'.format(self, path))

        @handle_response()
        def do():
            upload = functools.partial(self.core.upload_file, fileDir=path)
            ext = os.path.splitext(path)[1].lower()

            if ext in ('.bmp', '.png', '.jpeg', '.jpg', '.gif'):
                return upload(isPicture=True)
            elif ext == '.mp4':
                return upload(isVideo=True)
            else:
                return upload()

        return do().get('MediaId')


    # messages / register

    def _process_message(self, msg):
        """
        处理接收到的消息
'''
# def get_token():#凭借客户端凭据拿到访问令牌
#     server = "https://openapi.baidu.com/oauth/2.0/token?"
#     grant_type = "client_credentials"
#     #API Key
#     client_id = "cYLCFeB3xRH1fIocH4Pxcxgm"
#     #Secret Key
#     client_secret = "rSVho0KlHSuXZIyfAGGuNfmUkeOd7zsl"
#     #拼url
#     url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
#     #获取token
#     res = requests.post(url)
#     token = json.loads(res.text)["access_token"]
#     return token
#
# token = get_token()
# # file = "C:/Users/ASUS/Desktop/g16k.wav"
# def get_word(token,file): #使用访问令牌获取语音返回的文字
#     with open(file, "rb") as f:
#         speech = base64.b64encode(f.read()).decode('utf8')
#     size = os.path.getsize(file)
#     headers = { 'Content-Type' : 'application/json'}
#     url = "https://vop.baidu.com/server_api"
#     data={
#             "format":'wav',
#             "rate": 16000 ,
#             "dev_pid":1536,
#             "speech":speech,
#             "cuid":'baidu_workshop',
#             "len":size,
#             "channel":1,
#             "token":token,
#         }
#
#     req = requests.post(url,json.dumps(data),headers)
#     result = json.loads(req.text)
#     print(result)
#     ret=result["result"][0]
#     print(ret)
#     return ret
#
# token = get_token()
# ret = get_word(token,"C:/Users/ASUS/Desktop/16k [高质量].wav")
# print(ret)
# bot = Bot(cache_path= 'None')# 生成缓存文件wxpy.pkl后，为该文件路径
# tuling = Tuling(api_key='9d90c7fa414d4ae49362b99cfecedf4f')
# print('极简机器人已经启动')# 我的小号，测试需谨慎
# my_friednd = bot.friends().search('倪文')# 如果想对所有好友实现机器人回复把参数my_friend改成chats = [Friend]# 使用图灵机器人自动与指定好友聊天
# @bot.register(my_friednd)
# def reply_my_friednd(msg):
#     msg = '倪文 : 你好 (Text)'
#     #time.sleep(3)
#     tuling.do_reply(msg)# 进入交互式的 Python 命令行界面，并堵塞当前线程
# embed()


from io import BytesIO
from pydub import AudioSegment
from aip import AipSpeech
import pydub

import json
import urllib.request


api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我：')

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

        "selfInfo":
        {
            "location":
            {
                "city": "上海",
                "province": "上海",
                "street": "文汇路"
            }
        }
    },

    "userInfo":
    {
        "apiKey": "9d90c7fa414d4ae49362b99cfecedf4f",
        "userId": "OnlyUseAlphabet"
    }
}
# print(req)
# 将字典格式的req编码为utf8
req = json.dumps(req).encode('utf8')
# print(req)

http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(http_post)
response_str = response.read().decode('utf8')
# print(response_str)
response_dic = json.loads(response_str)
# print(response_dic)

intent_code = response_dic['intent']['code']
results_text = response_dic['results'][0]['values']['text']
print('Turing的回答：')
print('code：' + str(intent_code))
print('text：' + results_text)


#
# AudioSegment.from_mp3("C:/Users/ASUS/Desktop/16k.mp3")
# AudioSegment.export("C:/Users/ASUS/Desktop/16k.mp3",format="mp3", bitrate="256")
# pass
# def MP32WAV(mp3_path, wav_path):
#
#     # 这是MP3文件转化成WAV文件的函数
#     # :param mp3_path: MP3文件的地址
#     # :param wav_path: WAV文件的地址
#
#     pydub.AudioSegment.converter = "D:\\ffmpeg\\bin\\ffmpeg.exe"  # 说明ffmpeg的地址
#     MP3_File = AudioSegment.from_mp3(file=mp3_path)
#     MP3_File.export(wav_path, format="wav")
# MP32WAV("C:/Users/ASUS/Desktop/16k.mp3", "C:/Users/ASUS/Desktop/16k.wav")
# sound = AudioSegment.from_mp3("C:/Users/ASUS/Desktop/16k.mp3")
# a = sound.export("C:/Users/ASUS/Desktop/16k.wav",format ='wav')
# # # print(a)

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# import urllib2
# import time
# import urllib
# import json
# import hashlib
# import base64
# import urllib.request
# import urllib.parse
#
#
#
# def main():
#     f = open("C:/Users/ASUS/Desktop/16k (3).pcm", 'rb')  # rb表示二进制格式只读打开文件
#     file_content = f.read()
#     # file_content 是二进制内容，bytes类型
#     # 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
#     # 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
#     # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
#     base64_audio = base64.b64encode(file_content)  # base64.b64encode()参数是bytes类型，返回也是bytes类型
#     body = urllib.parse.urlencode({'audio': base64_audio})
#
#     url = 'http://api.xfyun.cn/v1/service/v1/iat'
#     api_key = '26afd791fcb3bb520e0151e6fc5440ad'
#     param = {"engine_type": "sms16k", "aue": "raw"}
#
#     x_appid = '5bff5bb4'
#     x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))  # 改('''')
#     # 这是3.x的用法，因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，
#     # 所以必须先转码为utf-8的bytes
#     x_param = str(x_param, 'utf-8')
#
#     x_time = int(int(round(time.time() * 1000)) / 1000)
#     x_checksum = hashlib.md5((api_key + str(x_time) + x_param).encode('utf-8')).hexdigest()  # 改
#     x_header = {'X-Appid': x_appid,
#                 'X-CurTime': x_time,
#                 'X-Param': x_param,
#                 'X-CheckSum': x_checksum}
#     # 不要忘记url = ??, data = ??, headers = ??, method = ?? 中的“ = ”，这是python3
#     req = urllib.request.Request(url=url, data=body.encode('utf-8'), headers=x_header, method='POST')
#     result = urllib.request.urlopen(req)
#     result = result.read().decode('utf-8')
#     print(result)
#     ret = re.findall(r'"data":"(.+?)"',result)[0]
#     print(ret)
#     return ret
#
#
# if __name__ == '__main__':
#     main()

# -*- coding: UTF-8 -*-
# import requests
# import time
# import urllib
# import json
# import hashlib
# import base64
#
# URL = "http://api.xfyun.cn/v1/service/v1/iat"
# APPID = '5bff5bb4'
# API_KEY = "26afd791fcb3bb520e0151e6fc5440ad"
#
#
# def getHeader():
#     # curTime = str(int(time.time()))
#     curTime = int(int(round(time.time() * 1000)) / 1000)
#     param = {"engine_type": "sms16k", "aue": "raw"}
#     paramBase64 = base64.b64encode(param)
#
#
#     m2 = hashlib.md5()
#     m2.update(API_KEY + curTime + paramBase64)
#     checkSum = m2.hexdigest()
#     header = {
#         'X-CurTime': curTime,
#         'X-Param': paramBase64,
#         'X-Appid': APPID,
#         'X-CheckSum': checkSum,
#     }
#     return header
#
#
# def main():
#     f = open("C:/Users/ASUS/Desktop/g15k.mp3", 'rb')
#     file_content = f.read()
#     base64_audio = base64.b64encode(file_content)
#     body = urllib.parse.urlencode({'audio': base64_audio})
#
#     r = requests.post(URL, headers=getHeader(), data=body.encode('utf-8'),  method='POST')
#     result = json.loads(r.content)
#
#     if result["code"] == "0":
#         print
#         "success, data = " + result["data"]
#     else:
#         print
#         r.text
#
#     return
#
#
# if __name__ == '__main__':
#     main()
