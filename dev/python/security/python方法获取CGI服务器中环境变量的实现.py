
#!/usr/bin/env python

import os

print 'Content-Type: text\html'

print '<h1>Server CGI Environment</h1></br>'

print '<ul>'

for param in os.environ.keys():
    print '<li>%s = %s</li>' % (param,os.environ[param])

print '</ul>'