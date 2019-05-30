import pymysql
from urllib.request import urlopen

db = pymysql.connect(host='localhost', port=3306, user='flask_user', passwd='flask_user', db='flaskdb', charset='utf8', autocommit=True)
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print("Database version : %s"%data)

db.close()

