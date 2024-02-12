import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    id=int(input("Enter id :"))
    name=input("Enter name :")
    sql="insert into user values ('%d','%s')"%(id,name)
    #cur.execute(sql)
    cur.execute(sql,id,name)
    con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()