#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-02 13:08:34
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Untitled-1
@Version: v0.1
@Description: 
'''

# import modules
import discord
from discord.ui import Select, View, Button
from discord.ext import commands

import datetime
import os

# Version
version = 'beta-0.1'
teamT1 = 0
teamDRX = 0

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def display_backend_info(author, content):
    print('-------------------------------------------')
    print('发送者:\t', author)
    print('完整内容:\t', content)
    print('当前时间:\t', datetime.datetime.now())
    print('-------------------------------------------')
  
# Client up
@client.event
async def on_ready():
    current_time = datetime.datetime.now()
    print(f'\n[开发人员]\t{client.user} 已登录...\n[USA BOS]\t', current_time,'\n')



# Client Event Trigger
@client.event
async def on_message(message):
    teamT1 = 0
    teamDRX = 0
    
    
    
    if message.author == client.user:
        return
    
    if message.content.startswith('$'):
        if message.content.startswith('$help'):
            help_msg = """
            === 食用手册 ===
1. $help\t查康指令
2. $welcome | $hello\t欢迎用语
3. $daily\t每日摸鱼!
4. $yyds\t凯老师 yyds!
5. $join\t追随比老师, 加入光荣的进化吧!
-------------------- TODO --------------------
6. $match 召唤师名称\t查看当前召唤师对局信息
7. $info\t查看当前发出消息者的对应联盟账号信息
8. $game\t小游戏合集 

            """
            await message.channel.send(help_msg)        
        
        elif message.content.startswith('$welcome') or message.content.startswith('$hello'):
            # await message.channel.send('欢迎老铁:\t{0}!'.format(message.author))
            
                
            selectMenu = Select(
                placeholder = "选择你的心动老师~",
                min_values= 1,
                max_values = 1,
                options=[
                    discord.SelectOption(label="凯老师", emoji="🍎",description="这是一个凯老师的介绍", default=False),
                    discord.SelectOption(label="比老师", emoji="🥕",description="这是一个比老师的介绍"),
                    discord.SelectOption(label="苏打老师", emoji="🍋",description="这是一个苏打老师的介绍"),
                    discord.SelectOption(label="贝老师", emoji="🍓",description="这是一个贝老师的介绍"),
                    discord.SelectOption(label="沈老师", emoji="🌰",description="这是一个沈老师的介绍")
                ]
            )
            
            view = View()
            view.add_item(selectMenu)
            
            async def selectMenuCallBack(interaction: discord.Interaction):
                
                #await interaction.response.edit_message(content =  selectMenu.values[0], view = None)
                #msg = "{0} 选择了 {1}".format(interaction.user, selectMenu.values[0])
                #await interaction.response.send_message(msg)
                if "凯" in selectMenu.values[0]: #and "ŁacusClyne#8619" == interaction.user
                    next_msg =  "{0}喝醉了, 居然给了自己一拳! 快去西方请沈老师救驾!".format(selectMenu.values[0])
                elif "比" in selectMenu.values[0]:
                    next_msg =  "今天我们讲的故事是, {0}和他的四个挂件上分的心路历程~".format(selectMenu.values[0])
                    
                elif "苏打" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)
                     
                    next_msg =  "{0}写代码已经走火入魔了, 神志不清ing! ".format(selectMenu.values[0])
                
                elif "贝" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)

                    next_msg =  "关于{0}矿里有家的故事代代相传~".format(selectMenu.values[0])
                elif "沈" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)
                     
                    next_msg =  "西天{0}专治各种疑难杂症.".format(selectMenu.values[0])
                else:
                    next_msg = "{0}非常高冷并给了你咣咣一👊!\n这就是小拳拳捶你胸口的威力嘛~".format(selectMenu.values[0])
                
                #await interaction.response.edit_message(view=None)
                #await interaction.followup.send(next_msg)
                await interaction.response.send_message(next_msg)
            selectMenu.callback = selectMenuCallBack

            
            await message.channel.send(view = view)

           
            
        elif message.content.startswith('$daily'):
            await message.channel.send('今天{0}摸鱼了没!'.format(message.author))
            
        elif message.content.startswith('$yyds'):
            await message.channel.send('凯老师 yyds!')
        
        elif message.content.startswith('$join'):
            await message.channel.send('加入光荣的进化吧!')
        
        elif message.content.startswith('$button'):
            button1 = Button(label="按钮1", url="https://www.baidu.com", style=discord.ButtonStyle.green, emoji="🍭")
            button2 = Button(label="按钮2",style=discord.ButtonStyle.green, emoji="🌰")
            button3 = Button(label="按钮3", style=discord.ButtonStyle.danger, emoji="⚽")
            
            async def button_callback(interaction:discord.Interaction):
                # await interaction.response.send_message("button2 已被点击")
                #isTimeout = await view.wait()
                # if isTimeout == True:
                    #button2.label = "new label"
                    #button.disabled = Trie
                    # await interaction.response.edit_message(content = "button2 已过期", view=None)
                # else:
                    
                await interaction.response.edit_message(content = "button2 已被点击", view=None)
                #await interaction.followup.send("next message send")
            button1.callback = button_callback
            button2.callback = button_callback
            button3.callback = button_callback
            view = View()#timeout = 5
            
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            
            #await message.channel.send("点击", view=view)
            await message.channel.send(view=view)
            
        elif message.content.startswith('$S12'):
            # button1 = Button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
            #button2 = Button(label="DRX",style=discord.ButtonStyle.green, emoji="🌰")
            
            
            
            @discord.ui.button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
            async def button_t1_callback(interaction:discord.Interaction):
                global teamT1
                global teamDRX
                teamT1 += 1
                
                result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)  
                   
                await interaction.response.edit_message(content = result)#view=None
                voter = "{0} 为 Team T1 贡献宝贵一票！ \n十年磨砺, 再夺一冠!".format(interaction.user)
                await interaction.followup.send(voter)

            @discord.ui.button(label="DRX", style=discord.ButtonStyle.green, emoji="🌰")
            async def button_drx_callback(interaction:discord.Interaction):
                global teamT1
                global teamDRX
                teamDRX += 1
                
                result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)      
                await interaction.response.edit_message(content = result)#view=None
                voter = "{0} 为 Team DRX 贡献宝贵一票！ \n三星十子，最后一舞!".format(interaction.user)
                await interaction.followup.send(voter)


            button1 = Button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
            button2 = Button(label="DRX",style=discord.ButtonStyle.green, emoji="🌰")
            
            button1.callback = button_t1_callback
            button2.callback = button_drx_callback
            #print(button_callback)
            view = View(timeout=600)#timeout = 5
            
            view.add_item(button1)
            view.add_item(button2)
            
            result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)
            await message.channel.send(result,view=view)  
        
        elif message.content.startswith('$game'):    
            selectMenu = Select(
                placeholder = "选个玩玩看吧~",
                min_values= 1,
                max_values = 1,
                options=[
                    discord.SelectOption(label="成语接龙", emoji="🍎",description="尾首相对 四字成语接龙", default=False),
                    discord.SelectOption(label="TBD", emoji="🥕",description="我还没想好(其实是偷懒没做)")
                ]
            )
            
            
            
            async def selectMenuCallBack(interaction: discord.Interaction):
                if "成语接龙" in selectMenu.values[0]:
                    reply = "贼喊捉贼"
                    msg = "游戏:\t成语接龙\n给出下一个:\t{0}".format(reply)
                    await interaction.response.edit_message(content = msg)
                elif "TBD":
                    await interaction.response.edit_message(content = "TBD 还未定~")
                else:
                    await interaction.response.edit_message(content = "出错啦!")
                
            selectMenu.callback = selectMenuCallBack

            view = View()
            view.add_item(selectMenu)
            
            await message.channel.send(view = view)
             
        else:
            await message.channel.send('抱歉还未学会这条命令~')
            
    #display_backend_info(message.author, message.content)
    
    
    
    
    
        
        
# Discord Bot Token
# Read from Token.txt file and keep it safe
token_file = open("./configs/Token.txt", "r")
token = token_file.read()
client.run(token)
