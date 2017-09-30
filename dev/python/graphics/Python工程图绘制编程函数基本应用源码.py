
# -*- coding:UTF8 -*-
#首先在犀牛5.0界面的命令行里面输入EditPythonScript
#在出来的界面复制粘贴这些代码
#把没用的注释掉,一个个试!一行行的慢慢自己看

import rhinoscriptsyntax as rs

def sums():
    a = rs.AddPoint((10,10,0)) #添加一个三维点
    b = rs.AddLine((0,0,0),(10,10,10)) # 两点确定一条直线
    c = rs.AddRectangle((0,0,0),10,20) # 中心点、长和宽
    d = rs.AddSphere((0,0,0),10) #圆心点、半径画球体
    e = rs.AddCircle((0,0,0),15) #圆心点、半径画圆型
    f = rs.AddCylinder((0,0,0),10,5,cap=True) #圆心点、高和半径画圆柱
    g = rs.AddCone((0,0,0),30,15) #圆心点、高和半径画圆锥
    h = rs.AddTorus((0,0,0),20,7,(10,10,10))# 大圆心大半径、小半径小圆心
    i = rs.AddArc((0,0,0),10,260) # 圆心点、半径、角度画弧线
    j = rs.AddEllipse((0,0,0),10,5) # 圆心点、半径、宽
    k = rs.AddSrfPt([(0,0,0),(10,0,0),(10,0,10),(0,0,10)])
    l = rs.AddText("道一",(0,0,0),font="幼圆",font_style=1,height=5.0) # 添加文本格式图像
    m = rs.AddPlanarMesh(e) # 调用e的方法 屏蔽其他的就流e和m
    n = rs.AddEllipse3Pt((0,0,0),(5,0,0),(0,10,0)) # 椭圆形
    o = rs.AddEllipse3Pt((0,0,0),(5,2,4),(4,5,7)) # 三维椭圆型
    p = rs.AddPlanarMesh(o) # 变形
sums()

