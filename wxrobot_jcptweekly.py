from threading import Timer
import requests
import random
import time
import schedule
import datetime


# markdown类型消息，发送到技术日报的群
def send_msg_txt_jsdaily(content):
    headers = {"Content-Type": "text/plain"}
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4d600608-4e56-404b-8138-82b7b42b523b"
    send_data = {
        "msgtype": "markdown",  # 消息类型，此时固定为text
        "markdown": {
            "content": content  # 文本内容，最长不超过2048个字节，必须是utf8编码
        }
    }

    requests.post(url=send_url, headers=headers, json=send_data)

# markdown类型消息，发送到技术周报的群
# def send_msg_txt_jsweekly(content):
#     headers = {"Content-Type": "text/plain"}
#     send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f03586c9-d895-4d08-b52b-ce9623fb007a"
#     send_data = {
#         "msgtype": "markdown",  # 消息类型，此时固定为text
#         "markdown": {
#             "content": content  # 文本内容，最长不超过2048个字节，必须是utf8编码
#         }
#     }
#
#     requests.post(url=send_url, headers=headers, json=send_data)


# 定义技术日报任务jsdaily_1
def send_jsdaily_1():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写日报啦**
<font color="comment">@xx@ </font>
#### 填写地址↓
>  【周计划与日报填写】[【技术周/日报】-手游发行业务_2020](https://shimo.im/sheets/nC7wScSyDicP6xGk/EEi1E)

#### 备注\n<font color="comment">①完成“</font><font color="info">✔周计划+✔日进展</font><font color="comment">“更新，更新后进行已更答复哈，谢谢</font>\n<font color="comment">②周计划摘自上周周报中的计划项，上周周报计划项未填写的请在此份中补全</font>
        '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_jsdaily(content.replace("@xx@", text))


# 定义技术日报任务jsdaily_14
def send_jsdaily_24():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写日报啦**
<font color="comment">@xx@ </font>
#### 填写地址↓
>  【日报填写】[【技术周/日报】-手游发行业务_2020](https://shimo.im/sheets/nC7wScSyDicP6xGk/EEi1E)

#### 备注\n<font color="comment">完成“</font><font color="info">日进展</font><font color="comment">”更新，更新后进行已更答复哈，谢谢</font>
        '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_jsdaily(content.replace("@xx@", text))

# 定义技术日报任务jsdaily_5
def send_jsdaily_5():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写周报啦**
<font color="comment">@xx@ </font>
#### 填写地址↓，请在今天下午15：00完成@所有人
>  【周进展与下周计划】[【技术周/日报】-手游发行业务_2021](https://shimo.im/sheets/nC7wScSyDicP6xGk/EEi1E)
#### 备注\n<font color="comment">完成“</font><font color="info">✔本周进展+✔下周计划</font><font color="comment">”更新，更新后进行已更答复哈，谢谢</font>
        '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_jsdaily(content.replace("@xx@", text))

def send_jsdaily_zj():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 没填写同学抽空填写下**
<font color="comment">@xx@ </font>
#### 填写地址↓
>  【请点击】[【技术周/日报】-手游发行业务_2021](https://shimo.im/sheets/nC7wScSyDicP6xGk/EEi1E)
#### 填写说明\n周一填写<font color="info">“周计划+日进展”</font>；周二~周四填写<font color="info">“日进展”</font>；周五填写<font color="info">“周总结+下周计划”</font>
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_jsdaily(content.replace("@xx@", text))

# def send_jsweekly_zj():
#     dt = time.strftime("%m-%d")
#     weeknum = datetime.datetime.now().isocalendar()[1]
#     weekday = time.strftime("%w")
#     text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"
#
#     content = '''
# # **🔥 没填写同学抽空填写下**
# <font color="comment">@xx@ </font>
# ### 👇报表地址
# >  【周五填写】[技术中心周报](https://shimo.im/sheets/vVqRVYyzNjh29Eqy/PbrNs)
# ### ✨填写说明\n周五填写<font color="info">“本周进展+下周计划”</font>
#     '''https://shimo.im/sheets/hrTt8P3ytjwVQVrg/UVWX7
#     # 打印下发送内容
#     print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
#     send_msg_txt_jsweekly(content.replace("@xx@", text))

# 定时每天某个时刻执行一次job函数
schedule.every().monday.at("15:00").do(send_jsdaily_1)
schedule.every().tuesday.at("15:00").do(send_jsdaily_24)
schedule.every().wednesday.at("15:00").do(send_jsdaily_24)
schedule.every().thursday.at("15:00").do(send_jsdaily_24)
schedule.every().friday.at("15:00").do(send_jsdaily_5)
schedule.every().monday.at("17:00").do(send_jsdaily_zj)
schedule.every().tuesday.at("17:00").do(send_jsdaily_zj)
schedule.every().wednesday.at("17:00").do(send_jsdaily_zj)
schedule.every().thursday.at("17:00").do(send_jsdaily_zj)
schedule.every().friday.at("17:00").do(send_jsdaily_zj)

while True:
    schedule.run_pending()  # 确保schedule一直运行
    time.sleep(2)
