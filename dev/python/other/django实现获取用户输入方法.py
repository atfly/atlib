
#urls.py
from django.conf.urls.defaults import *
from mysite.views import search , result
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', search),
    (r'^search/$', result)
)

#views.py
#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')
def result(request):
    key = request.GET['q']
    if not key :
        message = u'请输入搜索内容'
        return render_to_response('result.html',{'message':message})
    else :
        message = u'你输入的是' + key
        return render_to_response('result.html',{'message':message})


<html><!--search.html-->
<head>
    <title>Search</title>
</head>
<body>
    <form action="/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>

<html><!--result.html-->
<head>
    <title>Search</title>
</head>
<body>
        {{message}}
</body>
</html>