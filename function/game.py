#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-08 11:28:35
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\game.py
@Version: v1.0
@Description: 小游戏功能的实现与封装
'''

# import modules
import datetime
import os

# Coding here
def idiomDragon(input):
    """
    成语接龙小游戏
    规则: 前面一个成语的最后一个字和后面一个成语的第一个字需要相同
    @input: 从 Discord 消息中接收发送者的成语
    @result: 从 `Resource\chengyu.csv` 文件中读取符合规则的成语并返回给 Discord API 进行消息输出 
    """
    result = 1
    return result