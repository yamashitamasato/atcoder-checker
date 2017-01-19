#Copyright © 2017 山下正人. All rights reserved.
import asyncio
import aiohttp
import feedparser
import time
from bs4 import BeautifulSoup
import lxml
import sqlite3
atcoderG={}
atcoderR={}
atcoderB={}
atcoderT={}
res={}
#URLスクレイピング(非同期)
async def kaiseki(url,S):
    response = await aiohttp.request('GET', url)
    body = await response.text()
    soup = BeautifulSoup(body,'lxml')
    print(url,S,int(url[10:13]))
    i=url[10:13]
    resalt1=[]
    if(S=="b"):
        level = {"A": "No", "B": "No", "C": "No", "D": "No"}
    elif(S=="t"):
        level = {"A": "No", "B": "No", "C": "No"}
    elif(S=="r"):
        level = {"C": "No", "D": "No", "E": "No", "F": "No"}
    elif(S=="g"):
        level = {"A": "No", "B": "No", "C": "No", "D": "No","E":"No","F":"No"}
    for tbody in soup.findAll("tbody"):
        for td in tbody.findAll("tr"):
            tr=td.findAll("td")
            if(level[tr[1].text[0]]!="AC"):
                level[tr[1].text[0]]=tr[6].text

    for k, v in sorted(level.items()):
        resalt1.append(v)
    if(S=="b"):
        atcoderB.update({i:resalt1})
    elif(S=="t"):
        atcoderT.update({i:resalt1})
    elif(S=="r"):
        atcoderR.update({i:resalt1})
    elif(S=="g"):
        atcoderG.update({i:resalt1})
#URL設定
def start(username):
    dbname='database.db'
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    select_sql='select * from contest'
    loop = asyncio.get_event_loop()
    for row in c.execute(select_sql):
        S=row[0][0].lower()
        number=row[1]
        rss=[]
        for i in range(1,number+1):
            url = "http://a"+S+"c"+str(i).zfill(3)+".contest.atcoder.jp/submissions/all?user_screen_name="+username
            rss.append(url)
        loop.run_until_complete(asyncio.wait([kaiseki(url,S) for url in rss]))
    loop.close()
    conn.close()
    return atcoderB,atcoderG,atcoderR,atcoderT
if __name__ == '__main__':
    B,G,R,T=start('masahito')
