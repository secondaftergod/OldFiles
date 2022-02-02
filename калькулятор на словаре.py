import operator
a=float(input())
b=float(input())
c=input()
if (c=='/' or c=='div' or c=='mod') and b==0:
    print('Деление на 0!')
elif (c=='/' or c=='div' or c=='mod') and b!=0:
    op={'/':operator.truediv(a,b),'div':operator.floordiv(a,b),'mod':operator.mod(a,b)}
    print(op.pop(c))
else:
    op={'+':operator.add(a,b),'-':operator.sub(a,b),'*':operator.mul(a,b),'pow':operator.pow(a,b)}
    print(op.pop(c))

