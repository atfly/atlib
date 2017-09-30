
def timespent_processor(handler):       
    starttime = time.time()
    result = handler()
    web.ctx.timespent = timespent = time.time() - starttime
    content_type = dict(web.ctx.headers).get("Content-Type")
    xml_types = ("text/html", "application/xhtml+xml", "application/xml")
    if content_type in xml_types:
        result += "\n<!-- %d ms -->" % (timespent * 1000)
    return result

application.add_processor(timespent_processor)
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import json
import web

# ----------
# Processors
# ----------

def timespent_processor(handler):       
    starttime = time.time()
    result = handler()
    web.ctx.timespent = timespent = time.time() - starttime
    content_type = dict(web.ctx.headers).get("Content-Type")
    xml_types = ("text/html", "application/xhtml+xml", "application/xml")
    if content_type in xml_types:
        result += "\n<!-- %d ms -->" % (timespent * 1000)
    return result

# -----------
# Application
# -----------

urls = ("/", "Home",
        "/json/", "Json")

application = web.application(urls, globals())
application.add_processor(timespent_processor)

# -----------
# Controllers
# -----------

class Home(object):
    def GET(self):
        web.header("Content-Type", "text/html")
        return "<h1>Hello, World</h1>"

class Json(object):
    def GET(self):
        web.header("Content-Type", "application/json")
        return {'title': "Hello, World"}

# ------
# Runner
# ------

if __name__ == "__main__":
    application.run()
