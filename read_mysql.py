import pymysql
import pandas as pd
from smb.SMBConnection import SMBConnection

# 1.我们先建立数据库的连接信息
host = "10.59.105.19"  # 数据库的ip地址
db = "ads_monitor_3" # 数据表名称
user = "prog_select"  # 数据库的账号
password = "prog_select17173"  # 数据库的密码
port = 3310  # mysql数据库通用端口号

# 2.连接到数据库
conn = pymysql.connect(host=host,db =db,user=user,password=password,port=port) # 渠道三期数据库
conn_1 = pymysql.connect(host="10.59.67.213",db = "hyb",user = "hyb",password = "123") # hyb数据库

# 3.组装sql语句
# （命运神界，plid=4666落地页v2.00,prod_id=56命运神界SEM,m_id=167命运神界：梦境链接IOS预约，pt=317梦境链接预约）c_id =25564贴吧，25563广点通，25562微博，25561朋友圈，25560抖音
sql = '''SELECT c_id as '渠道' , pv , cur_date as '日期' FROM `day_common_202003` WHERE c_id in (25560,25561,25562,25563,25564)'''
sql_1 = '''
SELECT count(DISTINCT phone) as '预约手机数',FROM_UNIXTIME(created_at,"%Y%m%d")as '日期',client as '客户端',source as '来源'from `yy_phone` WHERE app='mysj' GROUP BY FROM_UNIXTIME(created_at,"%Y%m%d"),client,source
'''
# 4.获取需要数据

df = pd.read_sql(sql, conn)
df_1 = pd.read_sql(sql_1, conn_1)

# 5.另存为excel.k
writer = pd.ExcelWriter("d:/1.xlsx")  # 创建一张空表
df.to_excel(writer, sheet_name="命运神界_点击", encoding="UTF-8", freeze_panes=[1, 1])
df_1.to_excel(writer, sheet_name="命运神界_预约", encoding="UTF-8", freeze_panes=[1, 1])

writer.save()  # 保存新表内容
writer.close()
# 6.关闭数据库
conn.close()
conn_1.close()

# 7.建立samba链接
host = "samba.local.17173.com"   # ip或域名
username = "tlshouyou"
password = "TLshouyou.17!&#.com"
samba_conn = SMBConnection(username,password,"","",use_ntlm_v2 = True)
result = samba_conn.connect(host, 445)  # smb协议默认端口445
print("登录成功")


localFile = open("d:/1.xlsx", "rb")  # 需要上传的本地文件
samba_conn.storeFile("天龙手游", "素材报表/命运神界：梦境链接/mysjdata.xlsx", localFile)  # 需要上传到samba的哪个位置
localFile.close()
samba_conn.close()
# 关闭
print("上传成功")