

##############################################################
# import discord
# from discord.ui import Select, View, Button
# from discord.ext import commands


# Version
# version = 'beta-0.1'
# teamT1 = 0
# teamDRX = 0

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)

# def display_backend_info(author, content):
#     print('-------------------------------------------')
#     print('发送者:\t', author)
#     print('完整内容:\t', content)
#     print('当前时间:\t', datetime.datetime.now())
#     print('-------------------------------------------')
  
# # Client up
# @client.event
# async def on_ready():
#     current_time = datetime.datetime.now()
#     print(f'\n[开发人员]\t{client.user} 已登录...\n[USA BOS]\t', current_time,'\n')



# # Client Event Trigger
# @client.event
# async def on_message(message):
#     teamT1 = 0
#     teamDRX = 0
  
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('$'):
#         if '$help' in message.content:
#             help_msg = helpCommand.help(message.content)
#             await message.channel.send(help_msg)        
        
#         elif message.content.startswith('$welcome') or message.content.startswith('$hello'):
#             # await message.channel.send('欢迎老铁:\t{0}!'.format(message.author))
            
                
#             selectMenu = Select(
#                 placeholder = "选择你的心动老师~",
#                 min_values= 1,
#                 max_values = 1,
#                 options=[
#                     discord.SelectOption(label="凯老师", emoji="🍎",description="这是一个凯老师的介绍", default=False),
#                     discord.SelectOption(label="比老师", emoji="🥕",description="这是一个比老师的介绍"),
#                     discord.SelectOption(label="苏打老师", emoji="🍋",description="这是一个苏打老师的介绍"),
#                     discord.SelectOption(label="贝老师", emoji="🍓",description="这是一个贝老师的介绍"),
#                     discord.SelectOption(label="沈老师", emoji="🌰",description="这是一个沈老师的介绍")
#                 ]
#             )
            
#             view = View()
#             view.add_item(selectMenu)
            
#             async def selectMenuCallBack(interaction: discord.Interaction):
                
#                 #await interaction.response.edit_message(content =  selectMenu.values[0], view = None)
#                 #msg = "{0} 选择了 {1}".format(interaction.user, selectMenu.values[0])
#                 #await interaction.response.send_message(msg)
#                 if "凯" in selectMenu.values[0]: #and "ŁacusClyne#8619" == interaction.user
#                     next_msg =  "{0}喝醉了, 居然给了自己一拳! 快去西方请沈老师救驾!".format(selectMenu.values[0])
#                 elif "比" in selectMenu.values[0]:
#                     next_msg =  "今天我们讲的故事是, {0}和他的四个挂件上分的心路历程~".format(selectMenu.values[0])
                    
#                 elif "苏打" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)
                     
#                     next_msg =  "{0}写代码已经走火入魔了, 神志不清ing! ".format(selectMenu.values[0])
                
#                 elif "贝" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)

#                     next_msg =  "关于{0}矿里有家的故事代代相传~".format(selectMenu.values[0])
#                 elif "沈" in selectMenu.values[0]:#and "柠檬汽水不要汽水" in str(interaction.user)
                     
#                     next_msg =  "西天{0}专治各种疑难杂症.".format(selectMenu.values[0])
#                 else:
#                     next_msg = "{0}非常高冷并给了你咣咣一👊!\n这就是小拳拳捶你胸口的威力嘛~".format(selectMenu.values[0])
                
#                 #await interaction.response.edit_message(view=None)
#                 #await interaction.followup.send(next_msg)
#                 await interaction.response.send_message(next_msg)
#             selectMenu.callback = selectMenuCallBack

            
#             await message.channel.send(view = view)

           
            
#         elif message.content.startswith('$daily'):
#             await message.channel.send('今天{0}摸鱼了没!'.format(message.author))
            
#         elif message.content.startswith('$yyds'):
#             await message.channel.send('凯老师 yyds!')
        
#         elif message.content.startswith('$join'):
#             await message.channel.send('加入光荣的进化吧!')
        
#         elif message.content.startswith('$button'):
#             button1 = Button(label="按钮1", url="https://www.baidu.com", style=discord.ButtonStyle.green, emoji="🍭")
#             button2 = Button(label="按钮2",style=discord.ButtonStyle.green, emoji="🌰")
#             button3 = Button(label="按钮3", style=discord.ButtonStyle.danger, emoji="⚽")
            
#             async def button_callback(interaction:discord.Interaction):
#                 # await interaction.response.send_message("button2 已被点击")
#                 #isTimeout = await view.wait()
#                 # if isTimeout == True:
#                     #button2.label = "new label"
#                     #button.disabled = Trie
#                     # await interaction.response.edit_message(content = "button2 已过期", view=None)
#                 # else:
                    
#                 await interaction.response.edit_message(content = "button2 已被点击", view=None)
#                 #await interaction.followup.send("next message send")
#             button1.callback = button_callback
#             button2.callback = button_callback
#             button3.callback = button_callback
#             view = View()#timeout = 5
            
#             view.add_item(button1)
#             view.add_item(button2)
#             view.add_item(button3)
            
#             #await message.channel.send("点击", view=view)
#             await message.channel.send(view=view)
            
#         elif message.content.startswith('$S12'):
#             # button1 = Button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
#             #button2 = Button(label="DRX",style=discord.ButtonStyle.green, emoji="🌰")
            
            
            
#             @discord.ui.button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
#             async def button_t1_callback(interaction:discord.Interaction):
#                 global teamT1
#                 global teamDRX
#                 teamT1 += 1
                
#                 result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)  
                   
#                 await interaction.response.edit_message(content = result)#view=None
#                 voter = "{0} 为 Team T1 贡献宝贵一票！ \n十年磨砺, 再夺一冠!".format(interaction.user)
#                 await interaction.followup.send(voter)

#             @discord.ui.button(label="DRX", style=discord.ButtonStyle.green, emoji="🌰")
#             async def button_drx_callback(interaction:discord.Interaction):
#                 global teamT1
#                 global teamDRX
#                 teamDRX += 1
                
#                 result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)      
#                 await interaction.response.edit_message(content = result)#view=None
#                 voter = "{0} 为 Team DRX 贡献宝贵一票！ \n三星十子，最后一舞!".format(interaction.user)
#                 await interaction.followup.send(voter)


#             button1 = Button(label="T1", style=discord.ButtonStyle.red, emoji="🍭")
#             button2 = Button(label="DRX",style=discord.ButtonStyle.green, emoji="🌰")
            
#             button1.callback = button_t1_callback
#             button2.callback = button_drx_callback
#             #print(button_callback)
#             view = View(timeout=600)#timeout = 5
            
#             view.add_item(button1)
#             view.add_item(button2)
            
#             result = "T1:\t{0}\nDRX:\t{1}".format(teamT1,teamDRX)
#             await message.channel.send(result,view=view)  
        
#         elif message.content.startswith('$game'):    
#             selectMenu = Select(
#                 placeholder = "选个玩玩看吧~",
#                 min_values= 1,
#                 max_values = 1,
#                 options=[
#                     discord.SelectOption(label="成语接龙", emoji="🍎",description="尾首相对 四字成语接龙", default=False),
#                     discord.SelectOption(label="TBD", emoji="🥕",description="我还没想好(其实是偷懒没做)")
#                 ]
#             )
            
            
            
#             async def selectMenuCallBack(interaction: discord.Interaction):
#                 if "成语接龙" in selectMenu.values[0]:
#                     reply = "贼喊捉贼"
#                     msg = "游戏:\t成语接龙\n给出下一个:\t{0}".format(reply)
#                     await interaction.response.edit_message(content = msg)
#                 elif "TBD":
#                     await interaction.response.edit_message(content = "TBD 还未定~")
#                 else:
#                     await interaction.response.edit_message(content = "出错啦!")
                
#             selectMenu.callback = selectMenuCallBack

#             view = View()
#             view.add_item(selectMenu)
            
#             await message.channel.send(view = view)
        
#         # elif message.content.startswith('$chatGPT'):
#         #     msg = message.content.split("$chatGPT")[1]
#         #     code = chatGPT.AICodeCompletion(msg)
#         #     # TODO 暂时不管其他的 response，默认返回成功 只返回 code
#         #     result = "```python\n" + code + "\n```"
#         #     await message.channel.send(result)
        
#         elif message.content.startswith('$chatGPT'):
#             msg = message.content.split("$chatGPT")[1]
#             result = "..."
#             if "QA" in msg:
#                 msg_QA = msg.split("QA")[1]
                
#                 result = chatGPT.QAService(msg_QA)
#                 if "ERROR" in msg_QA:
#                     result = "Timeout 该 QA 程序超时(20S)，请更换问题或稍后再试~"
                
#             elif "code" in msg:
#                 msg_code = msg.split("code")[1]
#                 code = chatGPT.AICodeCompletion(msg_code)
#             # TODO 暂时不管其他的 response，默认返回成功 只返回回答
#                 result = "```\n" + code + "\n```"
#             await message.channel.send(result)   
        
#         elif message.content.startswith('$info'):# Lemon Sodà
            
#             name = message.content.split("$info")[1]
#             msg = league.displayTargetAccRankInfo(name)
#             if "Not Found" not in msg:    
#                 result = "==================== 🔥 ID: {0}\t账户信息 🔥 ====================\n<:transblanket:1039999774356688966> 账号: {1}\n<:lvl:1039999260541857832> 等级: {2}".format(name, msg['用户名'], msg['等级'])
                
#                 if 'SOLO' in msg:
#                     result = result + "\n++++++++++  单双  ++++++++++\n{0}\n<a:AnyaYay:1040000061033168978> 赢: {1}\n<a:UmaruChanCry:1040000749100343316> 输: {2}\n<:percent:1040001016759861379> 胜率: {3}".format(msg['SOLO']['单双'], msg['SOLO']['赢'],msg['SOLO']['输'],msg['SOLO']['胜率'])
#                 else:
#                     result = result + "\n++++++++++  单双  ++++++++++\nUnranked"
                
#                 if 'FLEX' in msg:
#                     win = "<a:AnyaYay:1040000061033168978>"
#                     result = result + "\n++++++++++  灵活  ++++++++++\n{0}\n<a:AnyaYay:1040000061033168978> 赢: {1}\n<a:UmaruChanCry:1040000749100343316> 输: {2}\n<:percent:1040001016759861379> 胜率: {3}".format(msg['FLEX']['灵活'], msg['FLEX']['赢'],msg['FLEX']['输'],msg['FLEX']['胜率'])
                
#                 else:
#                     result = result + "\n++++++++++  灵活  ++++++++++\nUnranked"
                
#                 result = result + "\n==================== 🔥 ID: {0}\t账户信息 🔥 ====================".format(name)
#                 await message.channel.send(result)
                
#             else:
#                 await message.channel.send('未找到相关账号，请仔细检查~')
                
#         elif message.content.startswith('$match'):
#             name = message.content.split("$match")[1]
#             msg = league.displayCurrentMatchPlayersInfo(name)
#             if msg != 'Target player is not in a game':
                
#                 begin_result = "==================== 🔥 ID: {0}\t当前对局 🔥 ====================".format(name)
#                 await message.channel.send(begin_result)
#                 for i in msg:
                    
#                     if "Not Found" not in msg[i]:    
#                         inner_result =  "\n<:transblanket:1039999774356688966> 账号: {0}\n<:lvl:1039999260541857832> 等级: {1}".format(msg[i]['用户名'], msg[i]['等级'])
                        
#                         if 'SOLO' in msg[i]:
#                             inner_result = inner_result + "\n\n单双: {0}\n<a:AnyaYay:1040000061033168978> 赢: {1}\n<a:UmaruChanCry:1040000749100343316> 输: {2}\n<:percent:1040001016759861379> 胜率: {3}".format(msg[i]['SOLO']['单双'], msg[i]['SOLO']['赢'],msg[i]['SOLO']['输'],msg[i]['SOLO']['胜率'])
#                         else:
#                             inner_result = inner_result + "\n\n单双: Unranked"
                        
#                         if 'FLEX' in msg[i]:
#                             win = "<a:AnyaYay:1040000061033168978>"
#                             inner_result = inner_result + "\n\n灵活: {0}\n<a:AnyaYay:1040000061033168978> 赢: {1}\n<a:UmaruChanCry:1040000749100343316> 输: {2}\n<:percent:1040001016759861379> 胜率: {3}".format(msg[i]['FLEX']['灵活'], msg[i]['FLEX']['赢'],msg[i]['FLEX']['输'],msg[i]['FLEX']['胜率'])
#                             await message.channel.send("--------------------------------------------------")
#                         else:
#                             inner_result = inner_result + "\n\n灵活: Unranked"
#                             await message.channel.send("--------------------------------------------------")
                        
#                         await message.channel.send(inner_result)
                        
#                     else:
#                         await message.channel.send('未找到相关账号，请仔细检查~')
                
                
#                 end_result = "\n==================== 🔥 ID: {0}\t当前对局 🔥 ====================".format(name)
                
#                 await message.channel.send(end_result)
#             else:
#                 await message.channel.send("🔥 ID: {0}\t当前没有在游戏中... 🔥".format(name))
               
#         else:
#             await message.channel.send('抱歉还未学会这条命令~')
            
#     # display_backend_info(message.author, message.content)
    
# client.run(getDiscordToken())
    
    
    
        
        

