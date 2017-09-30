
#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
0  All attributes off 默认值
1  Bold (or Bright) 粗体 or 高亮
4  Underline 下划线
5  Blink 闪烁
7  Invert 反显
30 Black text
31 Red text
32 Green text
33 Yellow text
34 Blue text
35 Purple text
36 Cyan text
37 White text
40 Black background
41 Red background
42 Green background
43 Yellow background
44 Blue background
45 Purple background
46 Cyan background
47 White background
"""
def main():
    """ """
for atrr in [0,1,4,5,7]:
    print "attribute %d ------------------------------" % atrr
    for fore in [30,31,32,33,34,35,36,37]:
        for back in [40,41,42,43,44,45,46,47]:
            color = "\x1B[%d;%d;%dm" % (atrr,fore,back)
            print "%s %d-%d-%d\x1B[0m" % (color,atrr,fore,back),
        print ""
if __name__ == "__main__":
    """ """
    main()