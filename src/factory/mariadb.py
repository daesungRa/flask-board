import pymysql

dbConn = pymysql.connect(host='localhost', port=3306, user='flask_user', passwd='0000', db='flaskdb', charset='utf8',
                         autocommit=True)

def autocomplete_result(query):
    with dbConn.cursor() as cursor:
        sql = "select id, country_code as data, country_name as value from countries where country_name like '%" + query + "%'"
        sql2 = "select id, country_code as data, country_name as value from countries where id between 20 and 39"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result
