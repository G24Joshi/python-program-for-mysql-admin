import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    cur.execute("select * from user")
    data=cur.fetchmany(3)
    print(data)
except Exception as ex:
    print(ex)
finally:
    con.close()