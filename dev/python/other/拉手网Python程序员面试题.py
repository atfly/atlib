
dic={}
def num(aa,bb,cc):
    if aa%bb==0:
        return cc
    else:
        return aa
def output(*ls):
    d=''
    if ls.count(ls[0])==len(ls):
        return ls[0]
    for i in ls:
        if i in dic.values():
            d=(d+i)
    return d

def execute(a,b,c,number=101):
    global dic
    dic=dict(zip([a,b,c],['Fizzy','Whizzy','Duzzy']))
    for i in range(1,number):
        print output(num(i,a,dic[a]),num(i,b,dic[b]),num(i,c,dic[c]))

if __name__=='__main__':
    execute(3,5,7)
