def build_graph(edges):
    edges = list(set(edges))
    graph = {}

    for edge in edges:
        frm = edge[:len(edge) - 1]
        to = edge[1:]
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]

    for val in graph.values():
        val.sort()

    return graph


def append_contig(graph, key):
    res = ''
    if len(graph[key]) > 1:
        for val in graph[key]:
            if val in graph:
                res += key[:1]
                res += append_contig(graph, val)
            else:
                res += '\n' + key[:1] + val
    else:
        res += key[:1] + graph[key][0]
    return res


if __name__ == '__main__':
    data = []
    for line in open('in.txt'):
        data.append(line.strip())
    graph = build_graph(data)

    for k, v in sorted(graph.items()):
        print(k + ' -> ' + ','.join(v))

    res = []
    for key in graph:
        res.append(append_contig(graph, key))

    with open('out.txt', 'w') as file:
        for i in sorted(res, key=lambda k: k[0]):
            print(i, file=file)
