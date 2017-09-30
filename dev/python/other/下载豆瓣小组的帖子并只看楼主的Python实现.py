
# Download douban group topic 
# Anonymous 2011-12@SZ

# 基本设置
post_url = "http://www.douban.com/group/topic/23871584/"
post_start =0
split_prefix = '<li class="clearfix">'
poster_user_id = ''
page_size = 100
save_filename = 'douban-post.txt'
log_falg = True

f = open(save_filename,'w')

# start 
import urllib2
import sys
import time

print 'Start ... '
html = urllib2.urlopen(post_url+"?start="+str(post_start)).read()

if html.index(split_prefix)<1:
	print 'This post has no content: url='+post_url+str(post_start)
	sys.exit(0)

cc = html.find('topic-content')
t_html = ''.join(html[cc:cc+150])
poster_user_id = t_html[t_html.index('people')+7: t_html.index('img')-4]
#www.iplaypy.com

c = 0
page = 0
while True:
	page += 1
	if log_flag: print '\npage=%d * %d' %(page,page_size)
	c = (page-1) * page_size

	# posts in current page
	posts = html.split(split_prefix)[1:]
	for p in posts:
		try:
			if (p.find('people/')>1):
				c += 1
				user_id = p[p.index('people/')+7:p.index('/"><img class="pil"')]
				if(user_id == poster_user_id):
					ss = '\n['+p[p.index('<h4>')+4:p.index('<h4>')+23] +" ]" +str(c)+"F "+ user_id + " : "+ p[p.index('<p>')+3:p.index('</p>')]
					if log_flag: print ss
					f.write(ss)
					f.flush()
		except ValueError:
			print '[error] Parse post error' 
			continue

	# next page
	post_start += page_size;
	html = urllib2.urlopen(post_url+"?start="+str(post_start)).read()
	if html.find(split_prefix)<1:
		if log_falg: print 'Post is over !'
		break

	time.sleep(3) # let douban server sleep 3 seconds .


f.close()
print 'Finished !'
