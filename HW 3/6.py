with open('in.txt', 'r') as f:
    a = f.read().split('\n')
graph = {}
for i in range(len(a)):
    a[i] = a[i].split(' -> ')
    graph[a[i][0]] = a[i][1].split(',')
ANS = []


def find_cycle(graph, v):
    while graph[v]:
        next = graph[v][0]
        graph[v].remove(next)
        # if len(graph[v])==0:
        #    graph.pop(v)
        find_cycle(graph, next)

    ANS.append(v)


find_cycle(graph, list(graph.keys())[0])
print("->".join(reversed(ANS)))
