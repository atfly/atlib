
class Entry( models.Model ):
    user = models.CharField(max_length=64)
    category = models.CharField(max_length=64 )
    title = models.CharField( max_length = 64 )
    entry_text = models.TextField()
    deleted_datetime = models.DateTimeField()

kwargs = {
    # 动态查询的字段
}

# 选择deleted_datetime为空的记录
if exclude_deleted:
    kwargs[ 'deleted_datetime__isnull' ] = True

# 选择特的category
if category is not None:
    kwargs[ 'category' ] = category

# 特定的用户
if current_user_only:
    kwargs[ 'user' ] = current_user

# 根据标题查询
if title_search_query != '':
    kwargs[ 'title__icontains' ] = title_search_query

# 应用所有的查询
entries = Entry.objects.filter( **kwargs )
# 打印出所有的结果检查
print entries 

#---------------www.iplaypy.com-----------------------------------
在这里要注意，如果用这种方式，在Q object方式下，是有问题的，要采用如下方式来处理。

kwargs = { 'deleted_datetime__isnull': True }
args = ( Q( title__icontains = 'Foo' ) | Q( title__icontains = 'Bar' ) )
entries = Entry.objects.filter( *args, **kwargs )
