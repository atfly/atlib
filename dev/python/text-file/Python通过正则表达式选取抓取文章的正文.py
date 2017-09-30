
#!/bin/env python

import re, sys

# Define parser first.
def baidu(username):
    # Business logic
    return "Using parser Baidu. and the user's name is: %s." % username

def qzone(uin):
    # Business logic
    return "Using parser Qzone, and the user's QQ is: %s." % uin

# From web.py
def group(seq, size):#{{{
    """
    Returns an iterator over a series of lists of length size from iterable.

        >>> list(group([1,2,3,4], 2))
        [[1, 2], [3, 4]]
        >>> list(group([1,2,3,4,5], 2))
        [[1, 2], [3, 4], [5]]
    """
    def take(seq, n):
        for i in xrange(n):
            yield seq.next()

    if not hasattr(seq, 'next'):
        seq = iter(seq)
    while True:
        x = list(take(seq, size))
        if x:
            yield x
        else:
            break
#}}}
#www.iplaypy.com

def parser_init(url,mapping):
    for pat, what in group(mapping,2):
        result = re.compile('^' + pat + '$').match(url)
        if result:
            return what, [x for x in result.groups()]
    return None, None

if __name__ == '__main__':
    mapping = (
            'http://(?:hi|space).baidu.com/([^/]+)(?:/.*)?','baidu',
            'http://(\d+).qzone.qq.com(?:/.*)?','qzone',
            )

    (func, args) = parser_init(sys.argv[1],mapping)
    if func:
        callback = func

        if func in globals():
            callback = globals()[func]

        if callable(callback):
            print callback(*args)
    else:
        print 'No parser found.';