
def time_span(ts):

   delta = datetime.now() - ts

   if delta.days >= 365:
       return '%d年前' % (delta.days / 365)

   elif delta.days >= 30:
       return '%d个月前' % (delta.days / 30)

   elif delta.days > 0:
       return '%d天前' % delta.days

   elif delta.seconds < 60:#www.iplaypy.com
       return "%d秒前" % delta.seconds
 
  elif delta.seconds < 60 * 60:
       return "%d分钟前" % (delta.seconds / 60)
 
  else:
       return "%d小时前" % (delta.seconds / 60 / 60)

