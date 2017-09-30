
import cx_Oracle   
  
dns_tns=cx_Oracle.makedsn("192.168.0.288",1521,"skynet")   
print dns_tns   

con = cx_Oracle.connect('alibaba', 'zhimakamen', dns_tns)   
cur=con.cursor()   

#www.iplaypy.com
  
for index,line in enumerate(file("f2.csv")):   
  sql="""insert into iq_data_B011F8286A1B2000A   
    (field1,field2,field3,field4) values ("""   

  for fields in (line.split(",")):   
    sql=sql+"'"+fields+"',"  
  cur.execute(sql[:-1]+")")   
  
con.commit()   
con.close()  