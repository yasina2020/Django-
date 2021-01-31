import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wu', db='django_test')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("select id,username,password from userinfo")
user_list = cursor.fetchall()

cursor.close()
conn.close()

print(user_list)
