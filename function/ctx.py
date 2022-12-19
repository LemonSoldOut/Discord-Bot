import interactions
import datetime

token = "MTAzNzQxMDU2OTM2NTQ5NTg5MA.G4vEYb.0qZ07XOsvOh9BZys6A_2m-LQUf_rIKSOL4nh_0"
bot = interactions.Client(token)


@bot.event
async def on_ready():
    current_time = datetime.datetime.now()
    print(f'\n[机器人]\t今日摸鱼 已上线...\n[USA BOS]\t', current_time,'\n')


@bot.command(
    name = "help",
    description = "今日摸鱼 Discord 机器人食用手册",
    scope = 671511786045964319)
async def help_command(ctx: interactions.CommandContext):
    await ctx.send("test")


@bot.command(
    name = "lol",
    description = "英雄联盟账号相关信息查询",
    scope = 671511786045964319,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "info",
            description = "当前账户信息",
            required = False
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "match",
            description = "当前对局信息",
            required = False
        )
    ]
)
async def league(ctx: interactions.CommandContext,info="", match=""):
    msg = ""
    #WARNING 这块代码需要重构！
    if info == "" and match == "":
        msg = "必须选择输入一个选项!"  
    if match != "":
        msg = msg + "match:\t{0}\n".format(match)
    if info != "":
        msg = msg + "info:\t{0}".format(info)
    
    await ctx.send(msg)
        

@bot.command(
    name = "ai",
    description = "ChatGPT: 智能 AI 聊天问答 , 编程, 翻译等功能",
    scope = 671511786045964319,
    
    options = [
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "chat",
            description = "聊天问答",
            required = False
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "code",
            description = "编程",
            required = False
        ),
        interactions.Option(
            type = interactions.OptionType.STRING,
            name = "translate",
            description = "翻译",
            required = False
        )
    ]
)    
async def chatGPT(ctx: interactions.CommandContext,chat="", code="", translate=""):
    msg = "chatGPT(ai)\n"
    if chat == "" and code == "" and translate == "":
        msg = "必须选择输入一个选项!"
    
    if chat != "":
        msg = msg + "聊天问答:\t{0}\n".format(chat)
    if code != "":
        msg = msg + "编程:\t{0}\n".format(code)
    if translate != "":
        msg = msg + "翻译:\t{0}".format(translate)
    
    await ctx.send(msg)
bot.start()
    