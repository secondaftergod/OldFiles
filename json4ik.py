import json4ik
final=dict()
fin=dict()
in_json=[{"name": "beta", "parents": ["alpha", "gamma"]}, {"name": "gamma", "parents": ["alpha"]}, {"name": "alpha", "parents": []}, {"name": "delta", "parents":["gamma", "zeta"]}, {"name": "epsilon", "parents":["delta"]}, {"name": "zeta", "parents":[]}]
#new_json=js = json.loads(in_json)
new_json=in_json

"""------------------------"""
for raw in new_json:
    for raw1 in raw['parents']:
        fin.setdefault(raw1,[])
        final.setdefault(raw1,1)
        final.setdefault(raw['name'],1)
        fin[raw1].append(raw['name'])

"""------------graph------------"""
import networkx as nx
G = nx.DiGraph()
for i,x in fin.items():
    G.add_node(i)
    for j in x:
        G.add_edge(i,j)
sp = dict(nx.all_pairs_shortest_path(G))

for i in fin.keys():
    final[i]+=len(sp[i])-1
"""--------------vizual----------"""
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
nx.draw(G, node_color='red',with_labels=True, font_weight='bold',node_size=1000)
plt.show()
#------------------------------
list_keys = list(final.keys())
list_keys.sort()
for i in list_keys:
    print(i,':',final[i])
