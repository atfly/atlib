
#encoding=utf-8

import web
import random
import os
import sae
import sae.const

web.config.debug = False

urls = ("/", "index",
           "/guess/","guess"
        )
def notfound():
    s=render.notfound()
    return web.notfound(s)

app_root = os.path.dirname(__file__)


app = web.application(urls, globals())
app.notfound=notfound

db = web.database(dbn='mysql', host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT),user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB)

store = web.session.DBStore(db, 'sessions')

templates_root = os.path.join(app_root, 'templates')

render = web.template.render(templates_root)

#www.iplaypy.com
session = web.session.Session(app, store, initializer={'count': 0,'answer':-1,'re':' ','start':0,'end':100})

class index:
    def GET(self):
        page= render.index('数字猜猜猜')
        return page
        
class guess:
    def GET(self):
        session.kill()
        result='开始猜数字吧'
        count=0
        start=0
        end=100
        page=render.game(result,count,start,end)
        return page
    def POST(self):
        try:
            data=web.input()
            nume=data.num
            session.count += 1
            a=session.answer
            num=int(nume)
            if a==-1:
                session.answer=random.randrange(100)
                a=session.answer
            if num>=int(session.end):
                session.re='超过范围了'
                session.count -= 1
            elif num<=int(session.start):
                session.re='超过范围了'
                session.count -= 1
            elif num<a:
                session.re='<img border=0 src="../static/smaller.png" />'
                session.start=num
            elif num>a:
                session.re='<img border=0 src="../static/biger.png" />'
                session.end=num
            else:
                session.re='<img border=0 src="../static/bingo.png" /><br/>答案是：'+str(a)
            db.insert('count',count=session.count)
            result=session.re
            count=session.count
            start=session.start
            end=session.end
            page=render.game(result,count,start,end)
            return page
        except:
            session.kill()
            result='输入有误，请重新开始吧'
            count=0
            start=0
            end=100
            page=render.game(result,count,start,end)
            return page


application = sae.create_wsgi_app(app.wsgifunc())