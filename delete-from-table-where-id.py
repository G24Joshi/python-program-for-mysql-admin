import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    id=int(input("Enter id :"))
    sql="delete from user where id='%d'"%(id)
    cur.execute(sql)
    con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()