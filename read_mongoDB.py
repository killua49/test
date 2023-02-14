import pymongo
import  pandas as pd

# 1.我们先建立数据库的连接信息
client = pymongo.MongoClient("mongodb://%s:%s@10.59.111.238:27017/?authSource=tlsylog&authMechanism=SCRAM-SHA-1" % (
    "prog_select", "prog_select17173"))

db = client['tlsylog']

# 查看已有数据集列表
print(db.list_collection_names())
# 查看已有数据库列表
#db.list_collection_names()

# 查询所有
#col.find()
# 条件查询
#col.find({'girlname':'兰追'})

