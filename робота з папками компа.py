import os
import os.path
os.chdir('sample')
answ=dict()
for current_dir,dirs,files in os.walk('.'):
    for i in files:
        name=os.path.splitext(i)[1]
        if name=='.py':
            answ.setdefault('sample'+current_dir.strip('.'))
os.chdir('/Users/ostap/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/main')
with open('out.txt','w') as file_out:
    file_out.write('\n'.join(sorted(answ)))
