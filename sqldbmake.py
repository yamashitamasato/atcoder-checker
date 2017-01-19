#Copyright © 2017 山下正人. All rights reserved.
#データベース構築
import sqlite3

dbname='database.db'

conn=sqlite3.connect(dbname)
c=conn.cursor()
create_table='''create table contest (contestname varchar(64),number int)'''

c.execute(create_table)

sql='insert into contest (contestname,number) values (?,?)'
contests = [
    ('Grand',1),
    ('Regular',1),
    ('Beginner',1),
    ('Typical',1)
]
c.executemany(sql,contests)
conn.commit()
conn.close()
