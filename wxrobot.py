from threading import Timer
import requests
import random
import time
import schedule
import datetime

# markdown类型消息，发送到业务日报的群
def send_msg_txt_ywdaily(content):
    headers = {"Content-Type": "text/plain"}
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8e2da700-53cc-4a37-9433-9684dc954df0"
    send_data = {
        "msgtype": "markdown",  # 消息类型，此时固定为text
        "markdown": {
            "content": content  # 文本内容，最长不超过2048个字节，必须是utf8编码
        }
    }

    requests.post(url=send_url, headers=headers, json=send_data)

# 定义业务发行日报任务ywdaily_1(周一计划)
def send_ywdaily_1():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写周进展+日报啦**
<font color="comment">@xx@ </font>
### 填写地址↓
>  【总汇总表】[手游发行业务-日/周报](https://shimo.im/sheets/XdVckHVg9JW3pdKy/XcVCb)\n
### 相关负责人，今日填写“周计划+当日进展”
<font color="info">●黎明之海：</font><font color="comment">〖PR〗@林乔；〖营销〗@葛琳琳；〖投放〗@智玺&@梁殷；〖运营〗@杨晓利；〖市场〗@李佳亮</font>
<font color="info">●极道市长：</font><font color="comment">@杨晓利</font> 
<font color="info">●龙与炼金师：</font><font color="comment">@朱林</font> 
<font color="info">●采购事项：</font><font color="comment">@黄冰冰</font> 
### 填写说明\n周一填写<font color="info">“周计划+日进展”</font>；周二~周四填写<font color="info">“日进展”</font>；周五填写<font color="info">“周总结”</font>
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))

# 定义业务发行日报任务ywdaily_24(周二四计划)
def send_ywdaily_24():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写日报啦**
<font color="comment">@xx@ </font>
### 填写地址↓
>  【总汇总表】[手游发行业务-日/周报](https://shimo.im/sheets/XdVckHVg9JW3pdKy/XcVCb)\n
### 相关负责人，今日填写“当日进展”
<font color="info">●黎明之海：</font><font color="comment">〖PR〗@林乔；〖营销〗@葛琳琳；〖投放〗@智玺&@梁殷；〖运营〗@杨晓利；〖市场〗@李佳亮</font>
<font color="info">●极道市长：</font><font color="comment">@杨晓利</font> 
<font color="info">●龙与炼金师：</font><font color="comment">@朱林</font> 
<font color="info">●采购事项：</font><font color="comment">@黄冰冰</font> 
### 填写说明\n周一填写<font color="info">“周计划+日进展”</font>；周二~周四填写<font color="info">“日进展”</font>；周五填写<font color="info">“周总结”</font>
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))

# 定义业务发行日报任务ywdaily_5(周五计划)
def send_ywdaily_5():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 写周报啦**
<font color="comment">@xx@ </font>
### 填写地址↓
>  【总汇总表】[手游发行业务-日/周报](https://shimo.im/sheets/XdVckHVg9JW3pdKy/XcVCb)\n
### 相关负责人，今日填写“本周总结”
<font color="info">●黎明之海：</font><font color="comment">〖PR〗@林乔；〖营销〗@葛琳琳；〖投放〗@智玺&@梁殷；〖运营〗@杨晓利；〖市场〗@李佳亮</font>
<font color="info">●极道市长：</font><font color="comment">@杨晓利</font> 
<font color="info">●龙与炼金师：</font><font color="comment">@朱林</font> 
<font color="info">●采购事项：</font><font color="comment">@黄冰冰</font> 
### 填写说明\n周一填写<font color="info">“周计划+日进展”</font>；周二~周四填写<font color="info">“日进展”</font>；周五填写<font color="info">“周总结”</font>
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))

# 定义业务发行日报任务ywdaily_zj(追加)
def send_ywdaily_zj():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 没填写同学抽空填写下**
<font color="comment">@xx@ </font>
### 填写地址↓
>  【总汇总表】[手游发行业务-日/周报](https://shimo.im/sheets/XdVckHVg9JW3pdKy/XcVCb)\n
### 填写说明\n周一填写<font color="info">“周计划+日进展”</font>；周二~周四填写<font color="info">“日进展”</font>；周五填写<font color="info">“周总结”</font>
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))


# 定时每天某个时刻执行一次job函数
schedule.every().monday.at("15:00").do(send_ywdaily_1)
schedule.every().tuesday.at("15:00").do(send_ywdaily_24)
schedule.every().wednesday.at("15:00").do(send_ywdaily_24)
schedule.every().thursday.at("15:00").do(send_ywdaily_24)
schedule.every().friday.at("15:00").do(send_ywdaily_5)
schedule.every().monday.at("17:00").do(send_ywdaily_zj)
schedule.every().tuesday.at("17:00").do(send_ywdaily_zj)
schedule.every().wednesday.at("17:00").do(send_ywdaily_zj)
schedule.every().thursday.at("17:00").do(send_ywdaily_zj)
schedule.every().friday.at("17:00").do(send_ywdaily_zj)

while True:
    schedule.run_pending()  # 确保schedule一直运行
    time.sleep(2)
