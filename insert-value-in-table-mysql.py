import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    cur.execute("insert into user values (101,'Amit')")
    con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()