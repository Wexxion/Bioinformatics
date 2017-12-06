# http://rosalind.info/problems/ba3e/


with open('in.txt', 'r') as f:
    a = f.read().split('\n')
graph = {}
for i in a:
    k = len(i)
    cur = i[:k - 1]
    if cur in graph:
        graph[cur].append(i[-k + 1:])
    else:
        graph[cur] = [i[-k + 1:]]
for i in graph:
    print("{} -> {}".format(i, ','.join(graph[i])))
