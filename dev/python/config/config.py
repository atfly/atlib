import pymysql
import configparser


# filePath = os.path.dirname(__file__) + '/../API/data/config.ini'
filePath ='C:/Users/wangwei/PycharmProjects/work/code_construct/Main_Scripts/data/config.ini'
# 读取配置文件
config = configparser.ConfigParser()
config.read(filePath)
ip = config.get("global", "host")
port = int(config.get("global", "port"))
user = config.get("global", "user")
passwd = config.get("global", "passwd")
db = config.get("global", "db")
charset = config.get("global", "charset")
