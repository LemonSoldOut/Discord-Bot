#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-11-08 11:25:18
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\league.py
@Version: v1.0
@Description: 英雄联盟 API 的相关使用与封装
'''

# import modules
import requests
import datetime
import yaml
import os

abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

# BUG: Windows path (not compatible for all platforms)

config_file_path = abs_path + "\\config\\config.yaml"
with open(config_file_path) as file:
    config = yaml.safe_load(file)

token = config['config']['lol']

# Coding here
def getLeagueAccountByName(name):
    headers = {f"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": token}
    
    url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    
    res = requests.get(url=url,headers=headers).json()
    if 'status' in res and res['status']['status_code'] == 404:
        return "Target Account Not Found"
    return res


def getLeagueAccountRankInfo(summoner_id):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": token}
    
    url = f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
    # url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/q9dWDdaT6Ctll-XnUecP1ubtwQSAu4qjA9UHv2V2LjRHgBA'
    
    res = requests.get(url=url,headers=headers).json()
    if res == []:
        return "Unranked"
    return res

def getCurrentMatchPlayers(name):
    res = getLeagueAccountByName(name)
    if "Target Account Not Found" in res:
        return res
    else:
        summoner_id = res['id']
        
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": token
    }
    url=f"https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}"
    
    
    res = requests.get(url=url,headers=headers).json()
    if 'status' in res and res['status']['message'] == 'Data not found':
        return "Target player is not in a game"
    
    json_players = res['participants']
    players = []
    for i in json_players:
        players.append(i['summonerName'])
    return players

def getCurrentMatchInfo():
    pass

def getTargetPlayerHistoryGames():
    pass

##############################################################
def displayTargetAccRankInfo(name):
    res = getLeagueAccountByName(name)
    if "Target Account Not Found" in res:
        return res
    else:
        summoner_id = res["id"]
    result = {}
    # result['id'] = summoner_id
    rankInfo = getLeagueAccountRankInfo(summoner_id)
    result["用户名"] = name
    result['等级'] = res['summonerLevel']
    
    if 'Unranked' in rankInfo:
        return result
    
    
    
    # if rankInfo['inactive'] == False:
    #     result["状态"] = "离线"
    # else:
    #     result["状态"] = "在线"
    
    for i in rankInfo:
        if i['tier'] == "IRON":
            tier = "<:lol_rank1_iron:1039995313370443816>"
        elif i['tier'] == "BRONZE":
            tier = "<:lol_rank2_bronze:1039995395931131934>"  
        elif i['tier'] == "SILVER":
            tier = "<:lol_rank3_silver:1039995459319644221>"
        elif i['tier'] == "GOLD":
            tier = "<:lol_rank4_gold:1039995514004979782>"
        elif i['tier'] == "PLATIMUM":
            tier = "<:lol_rank5_platinum:1039994915855282237>" 
        elif i['tier'] == "DIAMOND":
            tier = "<:lol_rank6_diamond:1039993080826310676>"  
        elif i['tier'] == "MASTER":
            tier = "<:lol_rank7_master:1039995627943239761>"     
        elif i['tier'] == "GRANDMASTER":
            tier = "<:lol_rank8_grandmaster:1039995705797910548>"  
        elif i['tier'] == "CHALLENGER":
            tier = "<:lol_rank9_challenger:1039995774349615198>"
        else:
            tier = "Unranked"  
        # if 'queueType' not in i:
        #     result["FLEX"] = {}
        #     result["FLEX"]["灵活"] = "Unranked"
        #     result["SOLO"] = {}
        #     result["SOLO"]["单双"] = "Unranked"
            
        if "FLEX" in i['queueType']:
            result["FLEX"] = {}    
            result["FLEX"]['灵活'] = f"{tier} {i['tier']} {i['rank']}  {i['leaguePoints']} 分"
            result["FLEX"]["赢"] = f"{i['wins']} 场"
            result["FLEX"]["输"] = f"{i['losses']} 场"
            win_rate = round(i['wins']/(i['losses'] + round(i['wins'])),2) * 100
            result["FLEX"]["胜率"] = f"{win_rate} %"
    
        elif "SOLO" in i['queueType']:
            result["SOLO"] = {}
            result["SOLO"]['单双'] = f"{tier} {i['tier']} {i['rank']}  {i['leaguePoints']} 分"
            result["SOLO"]["赢"] = f"{i['wins']} 场"
            result["SOLO"]["输"] = f"{i['losses']} 场"
            win_rate = round(i['wins']/(i['losses'] + round(i['wins'])),2) * 100
            result["SOLO"]["胜率"] = f"{win_rate} %"
    
            # if {rankInfo[0]['hotStreak']} == True:
            #     result["SOLO"]["是否连续上分"] = "是"
            # else:
            #     result["SOLO"]["是否连续上分"] = "否"
        else:
            return "N/A"
    
    
    # # result["老兵"] = f"{rankInfo[0]['veteran']}"
    # # result["新兵蛋子"] = f"{rankInfo[0]['freshBlood']}"
    
    return result
##############################################################
def displayCurrentMatchPlayersInfo(name):
    players = getCurrentMatchPlayers(name)
    result = {}
    for i in players:
        result[i] = displayTargetAccRankInfo(i)

    return result
##############################################################
# print(type(token))
# print(getLeagueAccountByName("UtopiaZeta"))
# print()
#print(displayCurrentMatchPlayersInfo("Maple Bookmark"))