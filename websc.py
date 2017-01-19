#Copyright © 2017 山下正人. All rights reserved.

import requests
from bs4 import BeautifulSoup
import lxml
import time
import sqlite3
session=requests.Session()
#データベースの値更新
def atsc():
    dbname='database.db'
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    contestlist={}
    select_sql='select * from contest'
    for row in c.execute(select_sql):
        print(row)
        S=row[0][0].lower()
        print(S)
        i=row[1]
        while True:
            url = "http://a"+S+"c"+str(i).zfill(3)+".contest.atcoder.jp"
            res = session.get(url)
            session.close()
            soup = BeautifulSoup(res.text.encode(res.encoding),"lxml")
            title = soup.find("h1").text
            if ('AtCoder' not in title):
                i-=1
                break
            else:
                i+=1
        contestlist[row[0]]=i
    for k, v in contestlist.items():
        update_sql="update contest set number = "+str(v)+" where contestname='"+k+"'"
        c.execute(update_sql)
    conn.commit()
    conn.close()
if __name__=="__main__":
    atsc()
