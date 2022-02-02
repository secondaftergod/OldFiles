a=input()
sum1=0
sum2=0
for z in str(a[:3]):
  sum1=sum1+int(z)
for i in str(a[3:6]):
    sum2=sum2+int(i)
if sum1==sum2:
    print('Счастливый')
else:
    print('Обычный')