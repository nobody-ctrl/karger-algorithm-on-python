import copy, random
import networkx as nx
import matplotlib.pyplot as plt


def contract(ver, e):
        print()
        print()
        print('[+] Starting the concatenation of nodes... until 2 are left')
        print()
        print()
        print()
        while len(ver) > 2:
                print()
                print()
                ind = random.randrange(0, len(e))
                [u, v] = e.pop(ind)
                print('[+] Concatenate:', u, 'and', v)
                ver.remove(v)
                ver.remove(u)
                ver.append(str(u) + 'and' + str(v))
                newEdge= []
                for i in range(len(e)):
                        if e[i][0] == v or e[i][0] == u:
                                e[i][0] = str(u) + 'and' + str(v)
                        elif e[i][1] == v or e[i][1] == u:
                                e[i][1] = str(u) + 'and' + str(v)
                        if e[i][0] != e[i][1]:
                                first = str(e[i][0])
                                sec = str(e[i][1])
                                if len(set(first.replace('and', '')) & set(sec.replace('and', ''))) == 0:
                                        newEdge.append(e[i])
                e = newEdge
                print('[+] Vertieces left:', ver)
                print('[+] Edges left:', e)
                print()
                print()
        print()
        print()
        print('[+] The algorithm is completed')
        print('[+++] Edges that are left: ', e)
        return len(e)


print('[+] Starting the program')
print('[+] Opening the file kargerMinCut.txt (note, that first numbers are node first and other symbolize edges...')
with open('kargerMinCut-version.txt', 'r') as infile:
        adjMat, edges, vertices = [], [], []
        for line in infile.readlines():
            one = line.split()
            for i in range(0, len(one)):
                one[i] = int(one[i])
            adjMat.append(one)
for i in range(len(adjMat)):
               s = adjMat[i]
               if(int(s[0]) not in vertices):
                    vertices.append(int(s[0]))
               for j in range(1, len(s)):
                       if [int(s[0]), int(s[j])] not in edges and [int(s[j]), int(s[0])] not in edges:
                                edges.append([int(s[0]), int(s[j])])
                       if int(s[j]) not in vertices:
                           vertices.append(int(s[j]))
print('[+] The grath is now created')
print('[+] Verticies:', vertices)
print('[+] Edges:', edges)
result = []
for i in range(10):
        print()
        print()
        print('[!] Attempt number', i)
        print()
        v = copy.deepcopy(vertices)
        e = copy.deepcopy(edges)
        r = contract(v, e)
        result.append(r)
print('[+] All the results we have became:', result)
print('[=] The minimum is', min(result))

G = nx.Graph()
G.add_edges_from(edges)
G.add_nodes_from(vertices)
nx.draw_networkx(G)
plt.show()