# http://rosalind.info/problems/ba3d/


def build_graph(edges):
    graph = {}

    for edge in edges:
        frm = edge[:-1]
        to = edge[1:]
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]

    for val in graph.values():
        val.sort()

    return graph


if __name__ == '__main__':
    file = open('in.txt')
    k = int(file.readline())
    string = file.readline()

    data = []
    for i in range(len(string)):
        if len(string[i:i + k]) == k:
            data.append(string[i:i + k])
    graph = build_graph(data)

    for k, v in sorted(graph.items()):
        print(k + ' -> ' + ','.join(v))

    with open('out.txt', 'w') as file:
        for k, v in sorted(graph.items()):
            print(k + ' -> ' + ','.join(v), file=file)
