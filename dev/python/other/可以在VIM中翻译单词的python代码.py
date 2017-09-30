
python << EOM
#coding = utf-8

def google_it(word):
    import re
    import webbrowser

    if not word or word.isspace():
        print 'there is no word under the cursor'
    else:
        try:
            url = 'http://www.google.com/search?q='+word
            webbrowser.open(url)
        except:
            print 'cannot access google!'
def google_translate_it(word):
    import re
    import webbrowser
    if not word or word.isspace():
        print 'there is no word under the cursor!'
    else:
        try:
            url = 'http://translate.google.cn/#en|zh-CN|'+word+'%0A'
            webbrowser.open(url)
        except:
            print 'cannot access google!'
EOM

#www.iplaypy.com

function! Google()
python << EOM
#coding = utf-8
import vim
py_word = vim.eval("expand(\"<cword>\")")
print py_word
google_it(py_word)
EOM
endfunction

function! GoogleTranslate()
python << EOM
#coding = utf-8
import vim
py_word = vim.eval("expand(\"<cword>\")")
print py_word
google_translate_it(py_word)
EOM
endfunction

command GOOGLE :call Google()
command GOOGLETRANSLATE :call GoogleTranslate()