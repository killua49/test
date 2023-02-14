from threading import Timer
import requests
import random
import time
import schedule
import datetime

# markdown类型消息，发送到业务日报的群
def send_msg_txt_ywdaily(content):
    headers = {"Content-Type": "text/plain"}
    send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=34863c20-5bfb-4741-9fc1-71623741fd8b"
    send_data = {
        "msgtype": "markdown",  # 消息类型，此时固定为text
        "markdown": {
            "content": content  # 文本内容，最长不超过2048个字节，必须是utf8编码
        }
    }

    requests.post(url=send_url, headers=headers, json=send_data)

# 定义业务发行日报任务ywdaily_1(周一计划)
def send_lmzhweekly_1():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 黎明之海周报更新**
<font color="comment">@xx@ </font>
### 请大家在18：00完成周报更新，填写地址↓
>  【版本时间线地址】[版本时间线](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/ep4CF)\n
>  【CB全视图地址】[CB全视图](https://www.processon.com/diagraming/5eaa4cb27d9c0869dab2afb6)\n
>  【Checklist地址】[Checklist](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/b3C9E)\n
>  【需要研发一起完成的地址】[需要研发一起完成的](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/NkVgC)\n
### 填写说明
<font color="info">〖版本时间线〗</font><font color="comment">@晓利</font>
<font color="info">〖CB全视图〗</font><font color="comment">@琳琳、@佳亮、@晓利、@智玺、@梁殷、@林恺、@昭宏</font>
<font color="info">〖Checklist〗</font><font color="comment">@琳琳、@佳亮、@晓利、@智玺、@梁殷、@林恺、@昭宏</font> 
<font color="info">〖需要研发一起完成的〗</font><font color="comment">@琳琳、@晓利、@林恺、@昭宏</font> 
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))

def send_lmzhweekly_zj():
    dt = time.strftime("%m-%d")
    weeknum = datetime.datetime.now().isocalendar()[1]
    weekday = time.strftime("%w")
    text = f"『周数』W-{weeknum} 『日期』{dt} 『星期』{weekday}"

    content = '''
# **🔥 没填写同学抽空填写下**
<font color="comment">@xx@ </font>
### 填写地址↓
>  【版本时间线地址】[版本时间线](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/ep4CF)\n
>  【CB全视图地址】[CB全视图](https://www.processon.com/diagraming/5eaa4cb27d9c0869dab2afb6)\n
>  【Checklist地址】[Checklist](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/b3C9E)\n
>  【需要研发一起完成的地址】[需要研发一起完成的](https://shimo.im/sheets/KlkKVeKgV2ulK2qd/NkVgC)\n
    '''
    # 打印下发送内容
    print("当前时间：%s，消息内容：%s" % (time.ctime(), "llll"))
    send_msg_txt_ywdaily(content.replace("@xx@", text))

# 定时每天某个时刻执行一次job函数
schedule.every().monday.at("10:30").do(send_lmzhweekly_1)
schedule.every().monday.at("17:00").do(send_lmzhweekly_zj)

while True:
    schedule.run_pending()  # 确保schedule一直运行
    time.sleep(2)
