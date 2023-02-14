import requests
import json
import pandas as pd

# 读取文件地址
df = pd.read_csv(r'E:\xlsx\命运神界7w+号码（去重）.csv')
phone = df['Mobile'].drop_duplicates()
for p in df['Mobile'].drop_duplicates():
    url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="+str(p)
    r1 = requests.post(url)
    print(r1.text)
# payload = {'tel': p}
# r1 = requests.post(url, json=payload)
# print(r1.text)

# data = json.dumps({'tel': phone[1]})
# r = requests.post(url, data, auth=('tel'))
# print (r.json)