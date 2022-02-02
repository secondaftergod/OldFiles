import networkx as nx
import re

# --------------z4utyv-----
a = list()
b=list()
with open('in.txt') as file_in:
    for line in file_in:
        line = line.strip()
        a.append(line)
with open('out.txt') as file_out:
  for line in file_out:
      line=line.strip()
      b.append(line)
#------------------------------
rez = list()
ver=list()
def sozd(umova):
    lst = re.findall(r'\w+', umova)
    if len(lst) == 2:
        rez.append([lst[1], lst[0]])
    elif len(lst) == 1:
        ver.append(lst[0])
    else:
        for i in range(len(lst) - 1):
            rez.append([lst[i + 1], lst[0]])
for i in a:
    sozd(i)

# ---------robota nad grafamu-------

G = nx.DiGraph()  # obizatilno tak 4utai dokumentaciu
for i in range(len(ver)):
    G.add_node(ver[i])
for i in range(len(rez)):
    G.add_edge(rez[i][0],rez[i][1])
#print(nx.dijkstra_path(G,))
print(G.nodes)
for i in b:
    lst=re.findall(r'\w+', i)
    if len(lst) == 2 and lst[0] in G.nodes:
        try:
            nx.dijkstra_path(G,lst[0],lst[1])
        except:
            print('No')
        else:
            print('Yes')
    elif lst[0] not in G.nodes:
        print('No')
    elif len(lst)==1 and lst[0] in G.nodes:
        print('Yes')
# ---------vizualizaci9-----------------

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
#------------------------------------------

import json4ik
# рекурсивная функция, создаёт множество, в которое добавляет все имена классов,
# которые являются потомком класса "class_name"
def test(class_name, set_):
    for dct in data_py:
        # если класс "class_name" является родителем класса dct['name'], то
        # добавляем класс "dct['name']" в множество "set_"
        if class_name in dct['parents']:
            set_.add(dct['name'])
        # вызываем эту же функцию от ребёнка класса "class_name",
        # таким образом спускаемся по древу предков и добавляем в set_ всех потомков
            set_ = test(dct['name'], set_)
    return set_
data_py = json4ik.loads(input())

# сортируем данный список словарей по именам ключей этих словарей
data_py.sort(key=(lambda x: x['name']))
# перебираем данный список
# выводим на экран "имя класса : длина множества имён всех предков",
# единицу прибавляем, так как в условии считается, что каждый класс является предком самому себе
for dct in data_py:
    print(dct['name'], ':', len(test(dct['name'], set())) + 1)