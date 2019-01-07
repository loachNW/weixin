import base64
import os
import os.path
import re
import time
import urllib.parse
from urllib import request

import itchat
import requests
from pydub import AudioSegment
from wxpy import *
from wxpy.api.messages.message import Message
from wxpy.compatible import *
import json
import urllib.request
import pydub
import io
import wave
import hashlib


def get_token():#凭借客户端凭据拿到访问令牌
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "cYLCFeB3xRH1fIocH4Pxcxgm"
    #Secret Key
    client_secret = "rSVho0KlHSuXZIyfAGGuNfmUkeOd7zsl"
    #拼url
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token

token = get_token()
def get_word(token,file): #使用访问令牌获取语音返回的文字
    with open(file, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')
    size = os.path.getsize(file)
    headers = { 'Content-Type' : 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data={
            "format":'wav',
            "rate": 8000 ,
            "dev_pid":1536,
            "speech":speech,
            "cuid":'baidu_workshop',
            "len":size,
            "channel":1,
            "token":token,
        }

    req = requests.post(url,json.dumps(data),headers)
    result = json.loads(req.text)
    print(result)
    ret=result["result"][0]
    print(ret)
    return result



def answer(question):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    text_input = question

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
                    "city": "长春",
                    "province": "吉林",
                    "street": "越达路"
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
    return (results_text)


def mp3_to_wav(mp3_path, wav_path):
    with open(mp3_path, 'rb') as fh:
        data = fh.read()

    aud = io.BytesIO(data)
    pydub.AudioSegment.converter = 'E:\\mysoft\\ffmpeg\\bin\\ffmpeg.exe'
    sound = pydub.AudioSegment.from_file(aud, format='mp3')
    raw_data = sound._data

    size = len(raw_data)
    f = wave.open(wav_path, 'wb')
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(16000)
    f.setnframes(size)
    f.writeframes(raw_data)
    f.close()

    return wav_path

def main(file):
    f = open(file, 'rb')  # rb表示二进制格式只读打开文件
    file_content = f.read()
    # file_content 是二进制内容，bytes类型
    # 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
    # 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
    # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    base64_audio = base64.b64encode(file_content)  # base64.b64encode()参数是bytes类型，返回也是bytes类型
    body = urllib.parse.urlencode({'audio': base64_audio})

    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    api_key = '26afd791fcb3bb520e0151e6fc5440ad'
    param = {"engine_type": "sms16k", "aue": "raw"}

    x_appid = '5bff5bb4'
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))  # 改('''')
    # 这是3.x的用法，因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，
    # 所以必须先转码为utf-8的bytes
    x_param = str(x_param, 'utf-8')

    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5((api_key + str(x_time) + x_param).encode('utf-8')).hexdigest()  # 改
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    # 不要忘记url = ??, data = ??, headers = ??, method = ?? 中的“ = ”，这是python3
    req = urllib.request.Request(url=url, data=body.encode('utf-8'), headers=x_header, method='POST')
    result = urllib.request.urlopen(req)
    result = result.read().decode('utf-8')
    print(result)
    ret = re.findall(r'"data":"(\w.+?)"',result)[0]
    print(ret)
    return ret


def MP32WAV(mp3_path, wav_path):
    """
    这是MP3文件转化成WAV文件的函数
    :param mp3_path: MP3文件的地址
    :param wav_path: WAV文件的地址
    """
    pydub.AudioSegment.converter = "D:\\ffmpeg\\bin\\ffmpeg.exe"  # 说明ffmpeg的地址
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File.export(wav_path, format="wav")


# 登录缓存路径,第一次设置为True
os.chdir('C:/Users/ASUS/Desktop/')
bot = Bot(cache_path= 'None')# 生成缓存文件wxpy.pkl后，为该文件路径
tuling = Tuling(api_key='9d90c7fa414d4ae49362b99cfecedf4f')
print('机器人已经启动')# 我的小号，测试需谨慎
#chats = [Friend]
my_friend = bot.groups().search('再不疯狂我们就老了')
# 发送消息# 如果想对所有好友实现机器人回复把参数my_friend改成chats = [Friend]# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friednd(msg):
    if msg.type == 'Recording':
        Message.get_file(msg,"C:/Users/ASUS/Desktop/16k.mp3")
        print('1111')
        sound = AudioSegment.from_mp3("C:/Users/ASUS/Desktop/16k.mp3")
        sound.export("C:/Users/ASUS/Desktop/16k.wav", format='wav')
        print('语音2')
        token = get_token()
        try:
            transform = get_word(token,"C:/Users/ASUS/Desktop/16k.wav")
            ret = answer(transform)
        except:
            try:
                Message.get_file(msg, "C:/Users/ASUS/Desktop/16k.pcm")
                transform = main("C:/Users/ASUS/Desktop/16k.pcm")
                ret = answer(transform)
            except:
                ret = "我耳朵可能坏掉了，没听清"
        # msg = Message(ret)
        # transform = main("C:/Users/ASUS/Desktop/16k.pcm")
        print(ret)
        return ret
    else:
        print(msg)
        # msg.download(msg['C:/Users/ASUS/Desktop/FileName'])   #这个同样是下载文件的方式
        # print(a)
        # msg['Text'](msg['C:/Users/ASUS/Desktop' + msg['FileName']])
        tuling.do_reply(msg)
itchat.auto_login(hotReload=None)
itchat.run()
