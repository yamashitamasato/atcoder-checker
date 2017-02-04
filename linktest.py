import asyncio
import aiohttp
from bs4 import BeautifulSoup
import lxml
import sqlite3
addURL=[]
notsubURL=[]
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
        notsubURL.append(url)

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
        loop.run_until_complete(asyncio.wait([urlpage(url,S) for url in rss]))
    loop.close()
    conn.close()
    print(addURL)
if __name__ == '__main__':
    start('masahito')
