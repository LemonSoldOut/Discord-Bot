#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-02 13:08:34
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord-Bot
@Version: beta-v0.1
@Description: Discord 多功能机器人
'''

# import modules
# Discord Interactions
# Github https://discord-interactions.readthedocs.io/en/latest/api.html

import interactions
from interactions import autodefer

import datetime
import os
import random
import yaml

import asyncio

from function import league
from function import helpCommand
from function import chatGPT
from util import utils
# Discord Bot Token
# Read from Token.txt file and keep it safe
# token_file = open("./config/Token.txt", "r")
# token = token_file.read()
def getToken(name:str):
    with open('./config/config.yaml') as file:
        config = yaml.safe_load(file)

    if name == "discord":
        token = config['config']['discord']["今日摸鱼"]
    elif name == "lol":
        token = config['config']['lol']
    elif name == "chatGPT":
        token = config['config']['chatGPT']
    elif name == "scope":
        token = config['config']['scope']["Eternal"]
    else:
        token = "ERROR"    
    return token


dicord_token = getToken("discord")
lol_token = getToken("lol")
chatGPT_token = getToken("chatGPT")
scope_id = getToken("scope")

bot = interactions.Client(dicord_token)
bot_name = "今日摸鱼"

os_name = utils.checkOperatingSystem()
embed_color_list = [0,1752220,1146986,5763719,2067276,3447003,2123412,10181046,7419530,15277667,11342935,15844367,12745742,15105570,11027200,15548997,10038562,9807270,9936031,8359053,12370112,3426654,2899536,16776960]

@bot.event
async def on_ready():
    current_time = datetime.datetime.now()
    print(f'\n[机器人]\t{bot_name} 已上线...\n[USA BOS]\t', current_time,f'\n[操作系统]\t{os_name}')


@bot.command(
    name = "help",
    description = "今日摸鱼 Discord 机器人食用手册",
    #scope = scope_id
)
@autodefer()
async def help_command(ctx: interactions.CommandContext):
    await asyncio.sleep(1)
    res = helpCommand.help()
    await ctx.send(res)
    
    

@bot.command(
    name = "game",
    description = "闲暇之际, 不来点小游戏开心一下?",
    #scope = scope_id
    options = [
        interactions.Option(
            type = interactions.OptionType.INTEGER,
            name = "choice",
            description = "输入数字: 1. 成语接龙 2. 猜大小 3. ToDo",
            required = True
        )
    ]
)
@autodefer()
async def help_command(ctx: interactions.CommandContext, choice:int):
    await asyncio.sleep(1)
    await ctx.send("还没做出来!")

@bot.command(
    name = "play",
    description = "音乐播放模块",
    #scope = scope_id
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "name",
            description = "网址 or BV (Todo 歌名)",
            required = False
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "source",
            description = "渠道(暂时默认 Bilibili)",
            required = False
        ),
    ]
)
@autodefer()
async def music_player(ctx: interactions.CommandContext, name:str, source="bilibili"):
    # await asyncio.sleep(3)
    
    # await ctx.send(g)
    # voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="C:\\Users\\lemon\\Desktop\\lemon\\Discord-Bot\\function\\music\\download.mp3"))
    
    random_number = random.randint(1,100)
    color_value = embed_color_list[random_number % len(embed_color_list)]
    # print(color_value)
    
    #Todo bot connect to voice channel
    #Todo bot play audio file
    # WARNING　目前来看，这个 Discord 模块并没有 audio和 voice channel 的功能
    # Github https://github.com/interactions-py/voice

    
    url = "https://fastly.jsdelivr.net/gh/lemonsoldout/pictures@main/16708321871771.jpeg"
    embeds = interactions.Embed(
                title="音乐模块",
                description="播放",
                color = color_value,
                image = interactions.EmbedImageStruct(
                    url = url,
                    height = 300,
                    width = 250,
                ),
                # author = interactions.EmbedAuthor(
                #     name="柠檬汽水不要汽水#5149",
                # ),
                # footer=interactions.EmbedFooter(
                #     text="这是一个脚注",
                # ),
                fields = [interactions.EmbedField(
                    name ="歌曲名",
                    value = "歌手名-时长",
                    inline = False,
                )],
                
    )
    await ctx.send(embeds=embeds)

@bot.command(
    name = "stop",
    description = "音乐模块",
)
@autodefer()
async def music_stop(ctx: interactions.CommandContext, source="bilibili"):
    await asyncio.sleep(1)
    
    random_number = random.randint(1,100)
    color_value = embed_color_list[random_number % len(embed_color_list)]
    # print(color_value)
    
    #Todo audio stop
    
    embeds = interactions.Embed(
                title="音乐模块",
                description="已停止",
                color = color_value,
    )
    await ctx.send(embeds=embeds)


@bot.command(
    name = "lol",
    description = "英雄联盟账号相关信息查询",
    #scope = scope_id,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "rule",
            description = "输入数字: 1. 当前活跃匹配查询 2. 账户信息查询",
            required = True
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "username",
            description = "账户名",
            required = True
        )
    ]
)
@autodefer()
async def league_command(ctx: interactions.CommandContext, rule:str, username:str):
    msg = ""
    
    if rule == "1":
        await asyncio.sleep(5)
        res = league.displayCurrentMatchPlayersInfo(username)
        if res in "Target Account Not Found":
            msg = "未找到用户!"
        
    elif rule == "2":
        await asyncio.sleep(5)
        res = league.displayTargetAccRankInfo(username)
        res = league.displayCurrentMatchPlayersInfo(username)
        if res in "Target Account Not Found":
            msg = "未找到用户!"
        else:
            msg = "用户名:\t{0}\n等级:\t{1}\n".format(res["用户名"], res["等级"])
            if "SOLO" in res:
                msg = msg + "单双:\t{0}\n赢:\t{1}\n输:\t{2}\n胜率:\t{3}".format(res["SOLO"]["单双"],res["SOLO"]["赢"],res["SOLO"]["输"],res["SOLO"]["胜率"])
        
    else:
        msg = "请输入正确的请求类型! 1. 当前活跃匹配查询 2. 账户信息查询"
    
    await ctx.send(msg)
        

@bot.command(
    name = "code",
    description = "ChatGPT: 编程代码相关功能的封装",
    #scope = scope_id,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "language",
            description = "编程语言",
            required = True
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "question",
            description = "问题",
            required = True
        ),
    ]
)    
@autodefer()
async def chatGPT_code(ctx: interactions.CommandContext, language:str, question:str):

    await asyncio.sleep(5)
    answer = chatGPT.AICodeCompletion(chatGPT_token, language, question)
    
    msg = "问题:\t{0}\n语言:\t{1}\n".format(question, language) + "```{0}\n{1}\n```".format(language,answer)

    random_number = random.randint(1,100)
    color_value = embed_color_list[random_number % len(embed_color_list)]

    # url = "https://fastly.jsdelivr.net/gh/lemonsoldout/pictures@main/16708321871771.jpeg"
    embeds = interactions.Embed(
                title="ChatGPT AI 模块",
                # description = question,
                color = color_value,
                # image = interactions.EmbedImageStruct(
                #     url = url,
                #     height = 300,
                #     width = 250,
                # ),
                # author = interactions.EmbedAuthor(
                #     name="柠檬汽水不要汽水#5149",
                # ),
                # footer=interactions.EmbedFooter(
                #     text="这是一个脚注",
                # ),
                fields = [interactions.EmbedField(
                    name = "编程",
                    value = msg,
                    inline = False,
                )],
                
    )
    await ctx.send(embeds=embeds)
    
    
@bot.command(
    name = "chat",
    description = "ChatGPT: AI 对话问答功能的封装",
    #scope = scope_id,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "question",
            description = "聊天问答",
            required = True
        )
    ]
)    
@autodefer()
async def chatGPT_chat(ctx: interactions.CommandContext, question:str):

    await asyncio.sleep(5)
    answer = chatGPT.chatService(chatGPT_token, question)
    msg = "{0}\n{1}".format(question, answer)
    
    random_number = random.randint(1,100)
    color_value = embed_color_list[random_number % len(embed_color_list)]
      
    embeds = interactions.Embed(
                title="ChatGPT AI 模块",
                color = color_value,
                fields = [interactions.EmbedField(
                    name = "聊天/问答",
                    value = msg,
                    inline = False,
                )],
                
    )
    await ctx.send(embeds=embeds)
    
    
    
@bot.command(
    name = "translate",
    description = "ChatGPT: 翻译功能的封装",
    #scope = scope_id,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "to",
            description = "目标语言: 中, 英, 日, 韩, 法, 德",
            required = True
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "content",
            description = "内容",
            required = True
        ),
    ]
)    
@autodefer()
async def chatGPT_translation(ctx: interactions.CommandContext, to:str, content:str):
    
    await asyncio.sleep(5)
    answer = chatGPT.translationService(chatGPT_token, to, content)
    msg = "原文:\t{0}\nTo:\t{1}文\n{2}".format(content, to, answer)
    
    random_number = random.randint(1,100)
    color_value = embed_color_list[random_number % len(embed_color_list)]
      
    embeds = interactions.Embed(
                title="ChatGPT 翻译模块",
                color = color_value,
                fields = [interactions.EmbedField(
                    name = "翻译",
                    value = msg,
                    inline = False,
                )],
                
    )
    await ctx.send(embeds=embeds)

# 启动 Discord 机器人   
bot.start()