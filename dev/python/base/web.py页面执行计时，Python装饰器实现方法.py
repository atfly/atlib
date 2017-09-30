
# coding=utf-8

from server import render

def display_time(func):
    import time

    def cal_time(*args):

        # 记录开始时间
        start = time.time()

        # 回调原函数
        result = func(*args)

        passtime = time.time() - start

        # 在结果输出追加计时信息
        result = result + "\n<!-- %s ms -->" % (passtime*1000)
        #www.iplaypy.com

        # 返回结果
        return result

    # 返回重新装饰过的函数句柄
    return cal_time

class Index(object):
    @display_time
    def GET(self):
        return render.home()