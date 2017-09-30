
>>> def getList(data):
	if isinstance(data,dict):
	    for i in data:
		path.append(i)
		getList(data[i])

>>> def set_value(path, dd, value):

    def get_path(path):
        if len(path):
            if len(path)==1:
                return {path[0]:value}
            return {path[0]:get_path(path[1:])}
    dd.update(get_path(path))
    return dd

>>> a =  {1:{2:{3:{4:{5:{6:{7:{8:9}}}}}}}}
>>> a

{1: {2: {3: {4: {5: {6: {7: {8: 9}}}}}}}}

>>> path = []
>>> getList(a)

>>> path
[1, 2, 3, 4, 5, 6, 7, 8]
>>> set_value(path,a,993)
{1: {2: {3: {4: {5: {6: {7: {8: 993}}}}}}}}