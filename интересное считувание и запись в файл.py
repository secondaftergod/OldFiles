lst=[]
with open('in.txt','r') as file_in, open('out.txt','w') as file_out:
    for i in file_in:
        lst.append(i.strip())
    lst.reverse()
    file_out.write('\n'.join(lst))




