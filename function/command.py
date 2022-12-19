#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-12-07 21:25:15
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\bot-command.py
@Version: v1.0
@Description: 设置 Discord 机器人内置命令
'''

# import modules


import requests

def setDiscordBotCommand():
    app_id = 1037410569365495890
    url = "https://discord.com/api/v10/applications/{0}/commands".format(app_id)
    
    command_name = "lol"
    
    # Help Discord 机器人の食用手册
    help_command = {
        "name": command_name,
        "type": 1,
        "description": "今日摸鱼 Discord 机器人の食用手册~",
        # "default_member_permissions": "0",
        "options": [
            {
                "name": "帮助手册",
                "description": "返回当前机器人的所有命令",
                "type": 3,
                "required": False,
            }
        ]
    }
    
    # chatGPT AI 功能命令
    chatGPT_command = {
            "name": command_name,
            "type": 1,
            "description": "智能 AI chatGPT 来进行对话，问答，翻译，代码编写等功能的实现~",
            # "default_member_permissions": "0",
            "options": [
                {
                    "name": "功能",
                    "description": "功能名称",
                    "type": 3,
                    "required": True,
                    "choices": [
                        {
                            "name": "编程 Code",
                            "value": "code"
                        },
                        {
                            "name": "翻译 Translate",
                            "value": "translate"
                        },
                        {
                            "name": "问答 QA",
                            "value": "QA"
                        },
                        {
                            "name": "对话 Chat",
                            "value": "chat"
                        }
                    ]
                },
                {
                    "name": "内容",
                    "description": "输入你想要的内容",
                    "type": 3,
                    "required": False
                }
            ]
        }
    
    # 英雄联盟功能
    lol_command = {
         "name": command_name,
        "type": 1,
        "description": "英雄联盟信息查询功能",
        # "default_member_permissions": "0",
        "options": [
            {
                "name": "lol",
                "description": "英雄联盟",
                "type": 3,
                "required": True,
                "choices": [
                    {
                        "name": "info",
                        "value": "账户信息"
                    },
                    {
                        "name": "match",
                        "value": "当前匹配"
                    },    
                ]
            },
        ]
    }

          
    # For authorization, you can use either your bot token
    headers = {
        "Authorization": "Bot MTAzNzQxMDU2OTM2NTQ5NTg5MA.G4vEYb.0qZ07XOsvOh9BZys6A_2m-LQUf_rIKSOL4nh_0"
    }

    res = requests.post(url, headers=headers, json=chatGPT_command)
    if res.status_code == 201:
        return {"SUCCESS" : f"command {command_name} created!"} 

    elif res.status_code == 200:
        return {"SUCCESS" : f"command {command_name} modified!"}
    else:
        return res.content

def getDiscordBotCommands():
    app_id = 1037410569365495890
    url = "https://discord.com/api/v10/applications/{0}/commands".format(app_id)
    
    headers = {
        "Authorization": "Bot MTAzNzQxMDU2OTM2NTQ5NTg5MA.G4vEYb.0qZ07XOsvOh9BZys6A_2m-LQUf_rIKSOL4nh_0"
    }
    
    res = requests.get(url, headers=headers).json()
    
    result = {}
    for i in res:
        result[i["id"]] = {}
        result[i["id"]]["命令"] = i["name"]
        result[i["id"]]["简介"] = i["description"] 
    
    return result

def delDiscordBotCommand(command_id):
    
    app_id = 1037410569365495890
    url = "https://discord.com/api/v10/applications/{0}/commands/{1}".format(app_id, command_id)
    
    headers = {
        "Authorization": "Bot MTAzNzQxMDU2OTM2NTQ5NTg5MA.G4vEYb.0qZ07XOsvOh9BZys6A_2m-LQUf_rIKSOL4nh_0"
    }
    
    res = requests.delete(url, headers=headers)
    if res.status_code == 204:
        return {"SUCCESS" : f"Target Command ID {command_id} Deleted!"}
    elif res.status_code == 404:
        return {"ERROR": f"Target Command ID {command_id} Not Found!"}
    else:
        return {"ERROR": "Something I didn't catch!"}


# 创建或修改命令
# print(setDiscordBotCommand())

# 获取所有已设置的命令
# print(getDiscordBotCommands())

# 删除指定 ID 的命令(ID 可从 getDiscordBotCommands() 中获取)
# print(delDiscordBotCommand(1050249766086385704))
