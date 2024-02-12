import pymysql
import pandas as pd
try:
    con=pymysql.connect(host="localhost",user="root",password="qwer1234",database="userdb132")
    cur=con.cursor()
    sql="select * from user"
    df=pd.read_sql(sql,con)
    print(df)
    df.to_csv("/tmp/mysql_users.csv",index=False)
    df.to_csv("/tmp/mysql_users.xlsx")
    #cur.execute(sql)
    #con.commit()
except Exception as ex:
    print(ex)
finally:
    con.close()