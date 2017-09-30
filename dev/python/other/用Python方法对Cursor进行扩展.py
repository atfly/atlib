
class BaseCursor(MySQLdb.cursors.BaseCursor):
    def _get_query_parameters(self, query, params):

        if isinstance(params, dict) and params:
            p = re.compile(':\w+')

            return (p.sub('%s', query),
                    [params[param_token[1:]] for param_token in p.findall(query)])
        else:
            return (query.replace('?', '%s'), params)

    def execute(self, query, args=None):
        (query, params) = self._get_query_parameters(query, args)

        return MySQLdb.cursors.BaseCursor.execute(self, query, params)

class Cursor(CursorStoreResultMixIn, CursorTupleRowsMixIn,
             BaseCursor):

#www.iplaypy.com
#调用的代码如下：
cursor=Cursor(self._dbconn)
try:
    cursor.execute('insert into users(name, domain)values(:name, :domain)', dict(name='xxx', domain='hahaha'))
    return cursor.lastrowid
finally:
    cursor.close()
