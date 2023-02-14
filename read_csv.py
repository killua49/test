import pandas as pd

# 读取文件地址
df = pd.read_csv(r'E:\xlsx\命运神界9w数据.csv')
phone = df['Mobile'].drop_duplicates()

d = {
    "移动": ['139', '138', '137', '136', '135', '134', '159', '150', '151', '158', '157', '188', '187', '152', '182',
           '147'],
    "联通": ['131', '132', '155', '156', '185', '186'],
    "电信": ['133', '153', '180', '189'],
    "虚拟": ['170']
}

#循环判断
u = {}   # 创建空字典
for k,i in d.items():  # 循环键值对
    for v in i:    # 键值对中值为列表，需要进行循环取出
        u[v] =k   # 进行键值的互换


#n = 0
for x in phone:
    s = str(x)  # 将手机号转成字符型
    if u.get(s[:3]):
        print(s[:11], s[:3], u.get(s[:3]))
    else:
#        n = n + 1
        print(s[:11], s[:3], '未知')