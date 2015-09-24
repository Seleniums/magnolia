#coding=utf-8

from modules.httpbase import HttpBaseHandler
from utils.tornado_extra import route
import pymysql
from common.tools import dictfetchall

@route('/')
class SayHello(HttpBaseHandler):
    def get(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='selenium', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM userinfo")
        rows = dictfetchall(cur)
        for row in rows:
            sex = row["sex"]
            self.write(sex)
            s = sex.encode('UTF-8')
            print(s)


        cur.close()
        conn.close()
        self.write('Hello World!')