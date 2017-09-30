
(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/css'}),
(r'^js/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/js'}),
(r'^images/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/images'}),

Django模板中使用下述方式即可：

<link href="/css/demo.css" type="text/css" rel="stylesheet">

需要注意的是：可采用os.path.dirname(globals()["__file__"])来获得当前文件所在路径。

看下面的例子：

(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"])+'/css'}),

可以使用os.path.abspath()函数，返回此路径的绝对路径。

=====www.iplaypy.com========

如果你想要在django的tempalte file中引用css、js、gif等静态文件，这时候你要做的是，首先一条setting.py中DEBUG开关打开。
1、在project目录下建立一个存放静态文件的目录，如：medias

2、在url.py patterns中增加一行：
   (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
   还要from django.conf import setting
3、在setting.py中加入一行：
   STATIC_PATH='./medias'

只有在如此设置后，就可以在template file 中引用media中存放的静态文件了，如：
   <img src='/site_media/django.gif'>
