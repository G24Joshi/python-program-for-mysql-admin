import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    data=[(103,"Ganesh"),(104,"Santosh"),(105,"Ravi"),(106,"Vijay")]
    sql="insert into user values (%s,%s)"
    cur.executemany(sql,data)
    con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()
