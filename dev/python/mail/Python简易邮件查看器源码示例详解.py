
#!/usr/bin/env python
# coding: utf-8

import os
import pygtk
import pango
pygtk.require('2.0')
import gtk
import email
import gobject

class FilesView(gtk.TreeView):
    def __init__(self):
        gtk.TreeView.__init__(self)

        self.model = self.__create_model()
        self.set_model(self.model)
        self.__add_column()

    def __create_model(self):
        model = gtk.ListStore(
                gobject.TYPE_STRING,
                gobject.TYPE_STRING)

        return model

    def __add_column(self):
        renderer = gtk.CellRendererText()
        column = gtk.TreeViewColumn(' ', renderer, text = 0)
        column.set_sort_column_id(0)
        self.append_column(column)

    def update_model(self, folder):
        files = os.listdir(folder)
        for file in files:
            fullpath = os.path.join(folder, file)

            self.model.append((file, fullpath))

class CheckMail(gtk.Window):

    def __init__(self, title = "简易Email查看器"):
        gtk.Window.__init__(self)

        self.set_title(title)
        self.set_size_request(640, 480)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", lambda *w: gtk.main_quit())

        hpaned = gtk.HPaned()
        self.add(hpaned)

        vbox = gtk.VBox(False, 5)
        vbox.set_size_request(200, -1)
        hpaned.pack1(vbox)

        self.treeview = gtk.TreeView()
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        vbox.pack_start(sw)

        self.treeview = FilesView()
        self.treeview.set_rules_hint(True)
        sw.add(self.treeview)

        button = gtk.Button("浏览")
        button.connect('clicked', self.on_browser_clicked)
        vbox.pack_start(button, False, False, 0)

        self.textbuffer = gtk.TextBuffer()
        self.textview = gtk.TextView(self.textbuffer)
        self.create_tags()
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        hpaned.pack2(sw)
        sw.add(self.textview)

        selection = self.treeview.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        selection.connect("changed", self.on_selection_changed)

        self.show_all()

    def on_selection_changed(self, widget, data = None):
        model, iter = widget.get_selected()
        fullpath = model.get_value(iter, 1)
        self.parse_mail(fullpath)

    def on_browser_clicked(self, widget):
        dialog = gtk.FileChooserDialog("Select a new folder", 
                action = gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_ACCEPT))
        dialog.set_current_folder(os.getenv("HOME"))
        if dialog.run() == gtk.RESPONSE_ACCEPT:
            folder = dialog.get_filename()

        dialog.destroy()

        self.treeview.update_model(folder)

    def create_tags(self):
        self.textbuffer.create_tag("big", size= 14 * pango.SCALE)

    def parse_mail(self, file):
        fp = open(file, "r")
        msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码
        mail_subject = msg.get("subject") # 取信件头里的subject,　也就是主题
        # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
        try:
            h = email.Header.Header(mail_subject)
            dh = email.Header.decode_header(h)
            mail_subject = dh[0][0]
        except UnicodeDecodeError:
            mail_subject = mail_subject.decode('gb2312')

        mail_from =  email.utils.parseaddr(msg.get("from"))[1] # 取from
        mail_to = email.utils.parseaddr(msg.get("to"))[1] # 取to

        for par in msg.walk():
            if not par.is_multipart(): 
            # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。

                name = par.get_param("name") #如果是附件，这里就会取出附件的文件名

                if name:# 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名

                    h = email.Header.Header(name)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    print '附件名:', fname
                    data = par.get_payload(decode=True) #解码出附件数据，然后存储到文件中
                   
                    try:
                        f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                    except:
        

                print '附件名有非法字符，自动换一个'
                        f = open('aaaa', 'wb')
                    f.write(data)
                    f.close()

                else:
                    #不是附件，是文本内容

                    mail_content = par.get_payload(decode=True) 
                    # 解码出文本内容，直接输出来就可以了。

                    break
               
        try:
            mail_subject = mail_subject.decode('gb2312')
        except UnicodeDecodeError:
            pass

        try:
            mail_from = mail_from.decode('gb2312')
        except UnicodeDecodeError:
            pass

        try:
            mail_to = mail_to.decode('gb2312')
        except UnicodeDecodeError:
            pass

        try:
            mail_content = mail_content.decode('gb2312')
        except UnicodeDecodeError:
            pass

        self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
        iter = self.textbuffer.get_iter_at_offset(0)
        self.textbuffer.insert_with_tags_by_name(iter, "标题：", "big")
        self.textbuffer.insert(iter, "%s\n" % mail_subject)
        self.textbuffer.insert_with_tags_by_name(iter, "发件人：", "big")
        self.textbuffer.insert(iter, "%s\n" % mail_from)
        self.textbuffer.insert_with_tags_by_name(iter, "收件人：", "big")
        self.textbuffer.insert(iter, "%s\n\n" % mail_to)
        self.textbuffer.insert_with_tags_by_name(iter, "正文：", "big")
        self.textbuffer.insert(iter, "\n%s" % mail_content)

        fp.close()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = CheckMail()
    hello.main()

