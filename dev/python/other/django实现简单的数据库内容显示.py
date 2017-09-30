
from django.http import HttpResponse
import os,sys
sys.path.insert(0,os.path.abspath(os.curdir))
import sqlite3
import settings
from ms.models import Student
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response


def archive(request):
    names = Student.objects.all()
    return render_to_response("index.html",locals())
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Upload Successfully</title>
	</head>
	<body>
		<p>所在城市</p>
		{% for name in names %}
		<p>{{name.city}}</p>
		<h2>1</h2>
		<p>{{name.name}}</p>
		<br>
		{% endfor %}
	</body>
</html>
