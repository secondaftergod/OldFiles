#n=int(input())
a=[]
with open('in.txt') as file_in:
  for line in file_in:
      line=line.strip()
      a.append(line)


space={'global':{'parametr':[],'parent':None}}

def create(newspace,nowspace):
  space.update({newspace: {'parametr': [], 'parent': nowspace}})

def add(kyda,chto):
  for i in space:
    if i==kyda:
      space[i]['parametr']+=[chto]

def get(namespace, chto):
  if chto in space[namespace]['parametr'] and namespace == 'global':
    print('global')
  elif chto in space[namespace]['parametr']:
    print(namespace)
  else:
    a=space[namespace]['parent']
    try:
      get(a, chto)
    except KeyError:
      print(None)


for i in a[1:]:
  cmd,a,b = i.split()
  if cmd=='create':
    create(a,b)
  elif cmd=='add':
    add(a,b)
  elif cmd=='get':
    get(a,b)







