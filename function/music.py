#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-08 11:25:15
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\Songs.py
@Version: v1.0
@Description: 歌曲功能的实现与封装
'''

# import modules
import datetime
import os
import asyncio
import youtube_dl
import requests
import re
import json
from lxml import etree

# Coding here
# yt_dl_opts = {'format':'bestaudio/best'}
# ytdl = youtube_dl.Youtubedl(yt_dl_opts)

# ffmpeg_options = {'options':'-vn'}




###############################################################################
video_url = "C:\\Users\\lemon\\Desktop\\1.mp4"


def extract_audio_from_video(video_url):
    output_audio_file = './music/output.mp3'
    if not os.path.exists(output_audio_file):
        # ffmpeg命令工具 在D:/FFmpeg/bin目录下
        try:
            # ffmpeg = r'D:/FFmpeg/bin/ffmpeg -i %s -vn -y -acodec copy %s' %(video_file,audio_file)
            # ffmpeg = r'D:/FFmpeg/bin/ffmpeg -i D:\AI\bili_data\test.mp4 -vn -y -acodec copy D:\AI\bili_data\output.aac'
            # 8000采样率
            ffmpeg = r'ffmpeg -i %s -f wav -vn -ar 8000 -ac 1 -y %s' % (video_url, output_audio_file)
            print("ffmpeg 命令: {0}".format(ffmpeg))
            os.system(ffmpeg)
            # p = subprocess.Popen(ffmpeg, shell=False)
            # p.wait(5)
            print('音频提取完成')
            os.remove(video_url)
            print("视频源已删除")
        except Exception as ex:
            print('音频提取异常', ex)
    else:
        print('该音频已存在，可以直接播放...')

    # 删除视频源
    

def download_audio_from_Bilibili(video_url):
    if 'https' not in video_url:
        video_url = "https://www.bilibili.com/video/" + video_url
        
    headers = {
        'Referer': 'https://www.bilibili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(video_url, headers).text
    tree = etree.HTML(response)
    pattern = '<script>window\.__playinfo__=(.*?)</script>' #提取音频url
    list_ = re.findall(pattern, response, re.S)
    list_json = json.loads(list_[0])
    
    # BUG 不知道为啥是个空的...
    # title = tree.xpath('//*[@id="viewbox_report"]/h1/span/text()') # 获取标题 index out of range
    # print("=====================================================\n",title) 
    
    volume_url = list_json['data']['dash']['audio'][0]['baseUrl']
    print(volume_url)
    PATH = './music/download.mp3' #保存路径
    audio = requests.get(url=volume_url, headers=headers).content
    with open(PATH, 'wb') as f:
        f.write(audio)
    print('音频下载完成')


download_audio_from_Bilibili("BV1aq4y1g7eo")

# Test
# url = input("Input Youtube URL\n")



# extract_audio_from_video(video_url)