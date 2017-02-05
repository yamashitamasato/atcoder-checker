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
addURL=[]
notsubURLlist=[]
#URLpageLink
async def urlpage(url,S):
    response = await aiohttp.request('GET', url)
    body = await response.text()
    soup = BeautifulSoup(body,'lxml')
    if (soup.find("div",class_="pagination pagination-centered")):
        divlink=soup.find("div",class_="pagination pagination-centered")
        spliturl=url.split("?")
        for i in divlink.findAll("a"):
            if(i.get_text().isdigit()):
                page=int(i.get_text())
        for i in range(1,page+1):
            addURL.append(spliturl[0]+"/"+str(1)+"?"+spliturl[1])
    else:
        notsubURLlist.append(url)


#URLスクレイピング(非同期)
async def kaiseki(url,S):
    response = await aiohttp.request('GET', url)
    body = await response.text()
    soup = BeautifulSoup(body,'lxml')

    i=url[10:13]
    resalt1=[]
    if(S=="b"):
        if(i in atcoderB):
            level=atcoderB.values(i)
        else:
            level = {"A": "No", "B": "No", "C": "No", "D": "No"}
    elif(S=="t"):
        if(i in atcoderT):
            level=atcoderT.values(i)
        else:
            level = {"A": "No", "B": "No", "C": "No"}
    elif(S=="r"):
        if(i in atcoderR):
            level=atcoderR.values(i)
        else:
            level = {"C": "No", "D": "No", "E": "No", "F": "No"}
    elif(S=="g"):
        if(i in atcoderG):
            level=atcoderG.values(i)
        else:
            level = {"A": "No", "B": "No", "C": "No", "D": "No","E":"No","F":"No"}
    for tbody in soup.findAll("tbody"):
        for td in tbody.findAll("tr"):
            tr=td.findAll("td")
            if(level[tr[1].text[0]]!="AC"):
                level[tr[1].text[0]]=tr[6].text

#    for k, v in sorted(level.items()):
#        resalt1.append(v)
    if(S=="b"):
        atcoderB.update({i:level})
    elif(S=="t"):
        atcoderT.update({i:level})
    elif(S=="r"):
        atcoderR.update({i:level})
    elif(S=="g"):
        atcoderG.update({i:level})

#URL設定
def start(username):
    dbname='database.db'
    conn=sqlite3.connect(dbname)
    c=conn.cursor()
    select_sql='select * from contest'
    loop = asyncio.get_event_loop()
    rss=[]
    for row in c.execute(select_sql):
        S=row[0][0].lower()
        number=row[1]

        for i in range(1,number+1):
            url = "http://a"+S+"c"+str(i).zfill(3)+".contest.atcoder.jp/submissions/all?user_screen_name="+username
            rss.append(url)
    loop.run_until_complete(asyncio.wait([urlpage(url,S) for url in rss]))

    loop.run_until_complete(asyncio.wait([kaiseki(url,url[8]) for url in addURL]))
    loop.close()
    conn.close()
    return atcoderB,atcoderG,atcoderR,atcoderT
if __name__ == '__main__':
    B,G,R,T=start('masahito')
