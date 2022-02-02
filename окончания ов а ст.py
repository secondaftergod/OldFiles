a=int(input())
n=[0,5,6,7,8,9,10,15,16,17,18,19,11,12,13,14,111,112,113,114,211,212,213,214,311,312,313,314,411,412,413,414,511,512,513,514,611,612,613,614,711,712,713,714,811,812,813,814,911,912,913,914]
def iskl():
    for i in n:
        if i==a:
            return True
def zel():
    if (a-1)%20==0 or (a-11)%20==0:
        return True
def bil():
    s,c=(a - (a // 20) * 20),((a-11) - ((a-11) // 20) * 20)
    if s==2 or s==3 or s==4 or c==1 or c==2 or c==3:
        return True
if zel() and not iskl():
    print(str(a)+' '+'программист')
elif bil() and not iskl() or a==32:
    print(str(a)+' '+'программиста')
else:
    print(str(a)+' '+'программистов')









