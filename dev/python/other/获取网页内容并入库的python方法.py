
#-*-coding:utf-8-*-
#encoding=utf-8

import sys;
import os;
import re;
import getopt;
import random;
import urllib2;
import time;
import datetime;
#import socket;
import MySQLdb as mysql;

reload(sys)

sys.setdefaultencoding('utf-8')

opts,argv = getopt.getopt(sys.argv[1:],'')

#urllib2.socket.setdefaulttimeout(15)

User = 'DB_User_Name'
Passwd = 'Password'
Host = 'localhost'
Db = 'DB_Name'

home = "http://zhidao.baidu.com/"

bmail = {'1':'@163.com','2':'@126.com','3':'@qq.com','4':'@gmail.com','5':'@sina.com.cn'}

im = {'1':'web','2':'wap','3':'mobile','4':'qq','5':'msn','6':'api','7':'sina','8':'qqwb','9':'vote' }


contents = mysql.connect(user=User,passwd=Passwd,host=Host,db=Db,charset='utf8')

sql_item = contents.cursor()

def Q ():
    q = re.sub(' ','',re.findall('<span class=\"question-title\">(.*?)</span>',qa_txt,re.DOTALL)[0])
    q_p = re.findall('<pre id=\"question-content\">(.*?)</pre>',qa_txt,re.DOTALL)
    q_pc = re.findall('<pre id=\"question-suply\">(.*?)</pre>',qa_txt,re.DOTALL)
    if q_p == [] and q_pc == []:
        return q
    elif q_p != [] and q_pc == []:
        return q+"\n"+re.sub(' ','',q_p[0])
    elif q_p == [] and q_pc != []:
        return q+"\n"+re.sub(' ','',q_pc[0])
    else:
        return q+"\n"+re.sub(' ','',q_p[0])+"\n"+re.sub(' ','',q_pc[0])


def QID ():
    return re.sub('<\/[a|A]>|<[a|A].*?>|\n|_$','',re.findall('<span class=\"gray\">\xcc\xe1\xce\xca\xd5\xdf\xa3\xba(.*?)<\/span>',qa_txt,re.DOTALL)[0])

def A ():
    return re.findall('<pre.*?>(.*?)<\/pre>',ac_txt[0],re.DOTALL)[0]

def AID ():
    if re.findall('<span class=\"gray\">\xbb\xd8\xb4\xf0\xd5\xdf\xa3\xba(.*?)<span class=\"v-split\">',ac_txt[0],re.DOTALL) == []:
        return "\xc8\xc8\xd0\xc4\xcd\xf8\xd3\xd1"
    else:
        return re.sub('<\/[a|A]>|<[a|A].*?>|\n|<span.*?>|\xc0\xb4\xd7\xd4\xcd\xc5\xb6\xd3|</span>| ','',re.findall('<span class=\"gray\">\xbb\xd8\xb4\xf0\xd5\xdf\xa3\xba(.*?)<span class=\"v-split\">',ac_txt[0],re.DOTALL)[0])

def getid (users):
    contgetid = mysql.connect(user=User,passwd=Passwd,host=Host,db=Db,charset='utf8')
    member_uid = contgetid.cursor()
    member_uid.execute("select `username`,`uid` from `sql_table_name`")
    contgetid.close();
    return dict(member_uid.fetchall()).get(users.decode('gbk','ignore'))

def weibo_id (wbid):
    weibo = mysql.connect(user=User,passwd=Passwd,host=Host,db=Db,charset='utf8')
    weibo_tid = weibo.cursor()
    weibo_tid.execute("select `roottid`,`tid` from `sql_table_name` where `content` like %s;","%"+wbid.decode('gbk','ignore')+"%")
    weibo.close();
    return weibo_tid.fetchall()

s = 1

while s:
    for sid in reversed(xrange(0,int(argv[0]),int(argv[1]))):
        for b in re.findall('<a href=\"\/question/(.*?)\.html\" title=\"',urllib2.urlopen("http://zhidao.baidu.com/browse/151?lm=0&word=&pn="+str(sid)).read(),re.DOTALL):
            request = urllib2.Request("http://zhidao.baidu.com/question/"+b+"\.html")
            request.add_header('User-Agent','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
            qa_txt = urllib2.urlopen(request).read()
            ac_txt = re.findall('<div class=\"content\">(.*?)<!--start test sns-->',qa_txt,re.DOTALL)
            if len(ac_txt) > 0:
                ask = Q()
                ask_id = QID()
                reply = A()
                reply_id = AID()
                #==构造 ASK_ID 入库参数==
                #print "1.",ask_id,"<====>",getid(ask_id)
                if getid(ask_id) == None :
                    member = ask_id.decode('gbk','ignore').encode('utf-8'),ask_id.decode('gbk','ignore').encode('utf-8'),str(int(random.uniform(1,3))),int(time.time()),int(time.time()),int(time.time()),str(int(random.uniform(1,3000))),ask_id.decode('gbk','ignore').encode('utf-8')+bmail.get(str(int(random.uniform(1,5))))
                    sql_item.execute("INSERT INTO `sql_table_name` (`uid`, `medal_id`, `media_id`, `username`, `nickname`, `password`, `secques`, `gender`, `regip`, `regdate`, `lastip`, `lastvisit`, `lastactivity`, `lastpost`, `oltime`, `pageviews`, `credits`, `extcredits1`, `extcredits2`, `extcredits3`, `extcredits4`, `extcredits5`, `extcredits6`, `extcredits7`, `extcredits8`, `email`, `bday`, `styleid`, `invisible`, `timeoffset`, `newpm`, `face_url`, `face`, `tag_count`, `role_id`, `role_type`, `new_msg_count`, `tag`, `own_tags`, `login_count`, `truename`, `phone`, `view_times`, `use_tag_count`, `create_tag_count`, `image_count`, `noticenum`, `ucuid`, `invite_count`, `invitecode`, `province`, `city`, `topic_count`, `at_count`, `follow_count`, `fans_count`, `email2`, `qq`, `msn`, `aboutme`, `at_new`, `comment_new`, `fans_new`, `topic_favorite_count`, `tag_favorite_count`, `disallow_beiguanzhu`, `validate`, `favoritemy_new`, `notice_at`, `notice_pm`, `notice_reply`, `user_notice_time`, `last_notice_time`, `theme_id`, `theme_bg_image`, `theme_bg_color`, `theme_text_color`, `theme_link_color`, `theme_bg_image_type`, `theme_bg_repeat`, `theme_bg_fixed`, `last_topic_content_id`) VALUES (null, '', 0, %s, %s, '4297f44b13955235245b2497399d7a93', '', %s, '', 0, '', %s, %s, %s, 0, 300, %s, 0, 30, 0, 0, 0, 0, 0, 0, %s, '0000-00-00', 0, 0, '', 0, '', '', 0, 3, 'normal', 0, '', 0, 1, '', '', 0, 1, 0, 0, 0, 0, 1, '35d69eddc4d041e8', '...', '..', 0, 0, 1, 1, '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 't6', '', '#C4CD58', '#333333', '#007FA9', 'center', 0, 0, 0);",member)
                    contents.commit()
                    print "Ask_Insert:",ask_id,"\t\t\tOK !"
                else:
                    pass

                #print "2.",reply_id,"<====>",getid(reply_id)
                if getid(reply_id) == None :
                    reply_member = reply_id.decode('gbk','ignore').encode('utf-8'),reply_id.decode('gbk','ignore').encode('utf-8'),str(int(random.uniform(1,3))),int(time.time()),int(time.time()),int(time.time()),str(int(random.uniform(1,3000))),reply_id.decode('gbk','ignore').encode('utf-8')+bmail.get(str(int(random.uniform(1,5))))
                    sql_item.execute("INSERT INTO `sql_table_name` (`uid`, `medal_id`, `media_id`, `username`, `nickname`, `password`, `secques`, `gender`, `regip`, `regdate`, `lastip`, `lastvisit`, `lastactivity`, `lastpost`, `oltime`, `pageviews`, `credits`, `extcredits1`, `extcredits2`, `extcredits3`, `extcredits4`, `extcredits5`, `extcredits6`, `extcredits7`, `extcredits8`, `email`, `bday`, `styleid`, `invisible`, `timeoffset`, `newpm`, `face_url`, `face`, `tag_count`, `role_id`, `role_type`, `new_msg_count`, `tag`, `own_tags`, `login_count`, `truename`, `phone`, `view_times`, `use_tag_count`, `create_tag_count`, `image_count`, `noticenum`, `ucuid`, `invite_count`, `invitecode`, `province`, `city`, `topic_count`, `at_count`, `follow_count`, `fans_count`, `email2`, `qq`, `msn`, `aboutme`, `at_new`, `comment_new`, `fans_new`, `topic_favorite_count`, `tag_favorite_count`, `disallow_beiguanzhu`, `validate`, `favoritemy_new`, `notice_at`, `notice_pm`, `notice_reply`, `user_notice_time`, `last_notice_time`, `theme_id`, `theme_bg_image`, `theme_bg_color`, `theme_text_color`, `theme_link_color`, `theme_bg_image_type`, `theme_bg_repeat`, `theme_bg_fixed`, `last_topic_content_id`) VALUES (null, '', 0, %s, %s, '4297f44b13955235245b2497399d7a93', '', %s, '', 0, '', %s, %s, %s, 0, 300, %s, 0, 30, 0, 0, 0, 0, 0, 0, %s, '0000-00-00', 0, 0, '', 0, '', '', 0, 3, 'normal', 0, '', 0, 1, '', '', 0, 1, 0, 0, 0, 0, 1, '35d69eddc4d041e8', '...', '..', 0, 0, 1, 1, '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 't6', '', '#C4CD58', '#333333', '#007FA9', 'center', 0, 0, 0);",reply_member)
                    contents.commit()
                    print "reply_Insert:",reply_id,"\t\t\tOK !"
                else:
                    pass

    		    #contents.close()

                #print "3.",ask_id,"<====>",getid(ask_id)
                if weibo_id(ask) == () :
                    inst_ask = getid(ask_id),ask_id.decode('gbk','ignore').encode('utf-8'),ask.decode('gbk','ignore').encode('utf-8'),int(time.time()),int(time.time()),im.get(str(int(random.uniform(1,9))))
                    sql_item.execute("INSERT INTO `sql_table_name` (`tid`, `uid`, `username`, `content`, `content2`, `imageid`, `videoid`, `musicid`, `roottid`, `replys`, `forwards`, `totid`, `touid`, `tousername`, `dateline`, `lastupdate`, `from`, `type`, `item_id`, `item`) VALUES (null, %s, %s, %s, '', 0, 0, 0, 0, 1, 0, 0, 0, '', %s, %s, %s, 'first', 0, '');",inst_ask)
                    contents.commit()
                    print "Ask_txt_Insert:",ask,"\t\t\t\tOK !"

                else:
                    pass


                #print "4.",reply_id,"<====>",getid(reply_id)
                if weibo_id(reply) == () :

                    #print weibo_id(ask)
                    if len(weibo_id(ask)) > 1 :
                        re_id = weibo_id(ask)[len(weibo_id(ask))-1]
                    elif len(weibo_id(ask)) == 1 :
                        re_id = weibo_id(ask)[0]
                    elif len(weibo_id(ask)) == 0 :
                        re_id = (0,0)

                    #print getid(reply_id)
                    inst_reply = getid(reply_id),reply_id.decode('gbk','ignore').encode('utf-8'),reply.decode('gbk','ignore').encode('utf-8'),str(re_id[1]),str(re_id[1]),getid(ask_id),ask_id.decode('gbk','ignore').encode('utf-8'),int(time.time()),int(time.time()),im.get(str(int(random.uniform(1,9))))
                    sql_item.execute("INSERT INTO `sql_table_name` (`tid`, `uid`, `username`, `content`, `content2`, `imageid`, `videoid`, `musicid`, `roottid`, `replys`, `forwards`, `totid`, `touid`, `tousername`, `dateline`, `lastupdate`, `from`, `type`, `item_id`, `item`) VALUES (null, %s, %s, %s, '', 0, 0, 0, %s, 0, 0, %s, %s, %s, %s, %s, %s, 'reply', 0, '');",inst_reply)
                    contents.commit
2966
()
                    print "Reply_txt_Insert:",reply,"\t\t\t\tOK !"
                else:
                    pass


                #同步评论
                #print ask,weibo_id(reply)
                if len(weibo_id(reply)) > 1 :
                    reply_re = weibo_id(reply)[len(weibo_id(reply))-1]
                elif len(weibo_id(reply)) == 1 :
                    reply_re = weibo_id(reply)[0]
                elif len(weibo_id(reply)) == 0 :
                    pass
                 
                #www.iplaypy.com
                #print len(reply_re[1])
                topic_more = str(reply_re[0]),"a:1:{i:0;s:"+str(len(str(reply_re[1])))+":\""+str(reply_re[1])+"\";}"
                #print topic_more
                topic_more_two = str(reply_re[1]),str(reply_re[0])
                #print topic_more_two
                sql_item.execute("INSERT INTO `sql_table_name` (`tid`, `parents`, `replyids`, `replyidscount`) VALUES (%s, '', %s, '1');",topic_more)
                sql_item.execute("INSERT INTO `sql_table_name` (`tid`, `parents`, `replyids`, `replyidscount`) VALUES (%s, %s, '', '0');",topic_more_two)
                #print weibo_id(reply)
                sql_item.execute("INSERT INTO `sql_table_name` (`tid` ,`replyid`) VALUES (%s, %s);",reply_re)
                print "Sync Reply OK!"

                print "============================================"
                time.sleep(int(random.uniform(30,320)))


            else:
                pass
            #time.sleep(int(random.uniform(100,200)))
        print "第",sid,"入库完成"
    print "所有采集完成,重新开始采集！"
contents.close()