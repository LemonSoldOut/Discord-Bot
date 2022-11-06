# Discord Bot
> Discord 多功能机器人 - 今日摸鱼
## 1. 环境准备
- 由于本机器人使用 Python 编程语言进行构建，所以我们所有环境都基于 Python 3.X 版本准备

1. [Python 3.X](https://www.python.org/downloads/)
2. 引入相关模块
    - 命令行输入 `pip install -r requirements.txt` 回车即可引入相关模块
    - ***注意！！！*** 当前 `requirements.txt` 中相关模块有很多无关模块也导入了，如果急需玩耍可以直接安装核心模块即可
        1. `pip install discord.py`
3. 准备一个 Discord 机器人或询问我获得机器人的 Token
    - 后面会补上如何注册 Discord 机器人
4. 运行机器人 
    - 单纯测试机器人: `python3 bot.py`，`CTRL` + `C` 即可退出程序
    - 后台运行机器人(推荐 Linux 系统): `python3 ./bot.py > discord-bot.log 2>&1 &`
        1. 在当前文件夹下创建 `discord-bot.log` 文件，并将所有后台日志存放于此文件中
        2. 后台运行 Python 程序，命令行返回一个 PID 进程号，请保管好这个 PID
            - 若粗心关闭当前界面，没有记住 PID 进程号，也可以重新打开命令行输入 `ps -aux|grep bot.py` 找到相关进程号(麻烦点)
        3. 若要关闭这个程序，命令行输入 `kill -9 PID` 即可关闭

## 2. 功能
### 2.1 信息交互

### 2.2 下拉框单/多选交互

### 2.3 按钮交互

### 2.4 TBD

## 3. TBD