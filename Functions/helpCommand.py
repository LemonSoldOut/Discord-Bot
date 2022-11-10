#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-10 17:03:13
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\help.py
@Version: v1.0
@Description: HELP 帮助手册
'''

# import modules
def help(command):
   
    return """
            ==================== 今日摸鱼 Bot の食用手册 =======================
1. $help 查康指令
2. $welcome | $hello\ 欢迎用语
3. $daily 每日摸鱼!
4. $yyds 凯老师 yyds!
5. $join 追随比老师, 加入光荣的进化吧!
-------------------- TEST --------------------
$info 查看当前发出消息者的对应联盟账号信息(基本可食用)
$match name 查看当前召唤师对局信息(测试ing)
-------------------- TODO --------------------
$play name/URL 通过指定歌曲名或 URL 读取音频源并播放
$pause 暂停当前歌曲的播放
$skip 跳过当前歌曲
$stop 停止播放音乐
$music list -a(-add) -d(-delete) -l(list) 添加/删除/列出歌单
----------------------------------------------
$game\t小游戏合集
$Todo ......
==================== 今日摸鱼 Bot の食用手册 =======================
"""