import requests
import json
import pandas as pd
import time
import datetime

dt = time.strftime("%Y-%m-%d")
weeknum = time.strftime("%W")
weekday = time.strftime("%w")
text = f"周数 ：W-{weeknum}，日期:{dt}，星期{weekday}"
print(text)
