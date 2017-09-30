
#!/usr/bin/env python

while 1:
   print "A.B.C.D"
   num1 = int(raw_input("Please input A:"))

   n1 =num1
   result1 = ''
   li1=[]
   while n1 >=16:
       if (n1%16)==10:
           li1.append("a")
       elif (n1%16)==11:
           li1.append("b")
       elif (n1%16)==12:
           li1.append("c")
       elif (n1%16)==13:
           li1.append("d")
       elif (n1%16)==14:
           li1.append("e")
       elif (n1%16)==15:
           li1.append("f")
       else:
           li1.append(n1%16)
       n1=n1/16
   if (n1)==10:
       li1.append("a")
   elif (n1)==11:
       li1.append("b")
   elif (n1)==12:
       li1.append("c")
   elif (n1)==13:
       li1.append("d")
   elif (n1)==14:
       li1.append("e")
   elif (n1)==15:
       li1.append("f")
   else:
       li1.append(n1)
   for i in range(0,len(li1)):
       result1+=str(li1[len(li1)-i-1])

   num2 = int(raw_input("Please input B:"))

   n2 =num2
   result2 = ''
   li2=[]
   while n2 >=16:
       if (n2%16)==10:
           li2.append("a")
       elif (n2%16)==11:
           li2.append("b")
       elif (n2%16)==12:
           li2.append("c")
       elif (n2%16)==13:
           li2.append("d")
       elif (n2%16)==14:
           li2.append("e")
       elif (n2%16)==15:
           li2.append("f")
       else:
           li2.append(n2%16)
       n2=n2/16
   if (n2)==10:
       li2.append("a")
   elif (n2)==11:
       li2.append("b")
   elif (n2)==12:
       li2.append("c")
   elif (n2)==13:
       li2.append("d")
   elif (n2)==14:
       li2.append("e")
   elif (n2)==15:
       li2.append("f")
   else:
       li2.append(n2)
   for j in range(0,len(li2)):
       result2+=str(li2[len(li2)-j-1])
   num3 = int(raw_input("Please input C:"))

   n3 =num3
   result3 = ''
   li3=[]
   while n3 >=16:
       if (n3%16)==10:
           li3.append("a")
       elif (n3%16)==11:
           li3.append("b")
       elif (n3%16)==12:
           li3.append("c")
       elif (n3%16)==13:
           li3.append("d")
       elif (n3%16)==14:
           li3.append("e")
       elif (n3%16)==15:
           li3.append("f")
       else:
           li3.append(n3%16)
       n3=n3/16
   if (n3)==10:
       li3.append("a")
   elif (n3)==11:
       li3.append("b")
   elif (n3)==12:
       li3.append("c")
   elif (n3)==13:
       li3.append("d")
   elif (n3)==14:
       li3.append("e")
   elif (n3)==15:
       li3.append("f")
   else:
       li3.append(n3)
   for k in range(0,len(li3)):
       result3+=str(li3[len(li3)-k-1])
   num4 = int(raw_input("Please input D:"))

   n4 =num4
   result4 = ''
   li4=[]
   while n4 >=16:
       if (n4%16)==10:
           li4.append("a")
       elif (n4%16)==11:
           li4.append("b")
       elif (n4%16)==12:
           li4.append("c")
       elif (n4%16)==13:
           li4.append("d")
       elif (n4%16)==14:
           li4.append("e")
       elif (n4%16)==15:
           li4.append("f")
       else:
           li4.append(n4%16)
       n4=n4/16
   if (n4)==10:
       li4.append("a")
   elif (n4)==11:
       li4.append("b")
   elif (n4)==12:
       li4.append("c")
   elif (n4)==13:
       li4.append("d")
   elif (n4)==14:
       li4.append("e")
   elif (n4)==15:
       li4.append("f")
   else:
       li4.append(n4)
   for h in range(0,len(li4)):
       result4+=str(li4[len(li4)-h-1])
   print "2001:778:0:ffff:64:0:"+result1+result2+":"+result3+result4