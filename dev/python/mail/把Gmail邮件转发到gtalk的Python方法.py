
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imaplib
import string, random
import StringIO, rfc822
import email
from google.appengine.api import xmpp


SERVER1 = "imap.gmail.com"

USER  = "yeah"
PASSWORD = "ohmyga"

# connect to server
server = imaplib(SERVER1, 993)

# login
server.login(USER, PASSWORD)
server.select()

# list items on server
status, data = server.search(None, "(UNSEEN)")

mails = data[0].split()

if data[0] != '':
    print "has  mails"
    user_address = 'wangnaide@gmail.com'

    for num in data[0].split():

        tpe, raw_msg = server.fetch(num, '(RFC822)')
        msg = email.message_from_string(raw_msg[0][1])

        #Subjects
        sbj, ecode = email.Header.decode_header(msg['subject'])[0]
        
        #from, sender
        frm = ''
        for fts, ecode in email.Header.decode_header(msg['from']):
            frm = frm + fts
        
        if xmpp.get_presence(user_address):
            xmpp.send_message(user_address, frm + ':' + sbj)
            server.store(num, '+FLAGS', '\\SEEN')
        #print frm + ":" + sbj

    
server.close()
server.logout()
