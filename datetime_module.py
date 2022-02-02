import datetime
import reZADACHI
lst=reZADACHI.findall(r'\w+', input())
data=datetime.date(int(lst[0]),int(lst[1]),int(lst[2]))
delta=datetime.timedelta(days=int(input()))
new=data+delta
print(new.strftime("%Y %-m %-d"))