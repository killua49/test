from smb.SMBConnection import SMBConnection
# 链接samba服务器
host="samba.local.17173.com"  #ip或域名
username="chanpin"
password="17173!chanpin"
samba_conn=SMBConnection(username,password,"","",use_ntlm_v2 = True)
result = samba_conn.connect(host, 445) #smb协议默认端口445
print("登录成功")

