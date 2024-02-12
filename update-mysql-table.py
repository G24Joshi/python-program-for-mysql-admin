import pymysql
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    id=int(input("Enter id :"))
    name=input("Enter name :")
    #sql="insert into user values ('%d','%s')"%(id,name)
    sql="update user set name='%s' where id='%d'"%(name,id)
    cur.execute(sql)
    con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()