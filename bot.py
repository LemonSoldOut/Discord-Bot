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
import interactions
from interactions import autodefer

import datetime
import os
import yaml

import asyncio

from Functions import league
from Functions import helpCommand
from Functions import chatGPT

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

@bot.event
async def on_ready():
    current_time = datetime.datetime.now()
    print(f'\n[机器人]\t今日摸鱼 已上线...\n[USA BOS]\t', current_time,'\n')


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
    name = "music",
    description = "闲暇之际, 不来点小游戏开心一下?",
    #scope = scope_id
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "action",
            description = "执行的操作",
            required = True
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "name",
            description = "歌名",
            required = True
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "source",
            description = "渠道(前期应该默认只有一个音乐的 API 封装吧)",
            required = False
        ),
    ]
)
@autodefer()
async def help_command(ctx: interactions.CommandContext, action:str, name:str, source=""):
    await asyncio.sleep(1)
    await ctx.send("还没做出来!")

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
    await ctx.send("暂时无法使用, maybe 明天修复! (也许吧...)")
    # if rule == "1":
    #     await asyncio.sleep(5)
    #     res = league.displayCurrentMatchPlayersInfo(username)
    #     if res in "Target Account Not Found":
    #         msg = "未找到用户!"
        
    # elif rule == "2":
    #     await asyncio.sleep(5)
    #     res = league.displayTargetAccRankInfo(username)
    #     res = league.displayCurrentMatchPlayersInfo(username)
    #     if res in "Target Account Not Found":
    #         msg = "未找到用户!"
    #     else:
    #         msg = "用户名:\t{0}\n等级:\t{1}\n".format(res["用户名"], res["等级"])
    #         if "SOLO" in res:
    #             msg = msg + "单双:\t{0}\n赢:\t{1}\n输:\t{2}\n胜率:\t{3}".format(res["SOLO"]["单双"],res["SOLO"]["赢"],res["SOLO"]["输"],res["SOLO"]["胜率"])
        
    # else:
    #     msg = "请输入正确的请求类型! 1. 当前活跃匹配查询 2. 账户信息查询"
    # await ctx.send(msg)
        

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

    await ctx.send(msg)
    
    
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
    msg = "聊天/问答:\t{0}\n{1}".format(question, answer)
        
    await ctx.send(msg)
    
    
    
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
    msg = "翻译:\t{0}\n目标语言:\t{1}文\n{2}".format(content, to, answer)
        
    await ctx.send(msg)


# 启动 Discord 机器人   
bot.start()