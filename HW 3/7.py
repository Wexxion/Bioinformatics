with open('in.txt', 'r') as f:
    a = f.read().split('\n')
k = int(a[0].split()[0])
d = int(a[0].split()[1])
paires = []


def check_pairs(f, s):
    if (f[0][-k + 1:] == s[0][:k - 1]) and (f[1][-k + 1:] == s[1][:k - 1]):
        return True


def get_pairs(pairs):
    gr = {}
    for x in range(0, len(paires), 1):
        for y in range(0, len(paires), 1):
            if x != y and check_pairs(paires[x], paires[y]):
                gr[x] = y
    return gr


def find_start(pares, a):
    key = pares.values()
    for x in range(len(a)):
        if not x in key:
            return x


def find_end(pares, a):
    key = pares.keys()
    for x in range(len(a)):
        if not x in key:
            return x


def get_superstring(start, end, paires, gp):
    res = [None] * (len(a) - 1 + 2 * k + d - 1)
    cur = start
    ind = 0
    while True:
        cur_p = paires[cur]
        for s in cur_p[0]:
            res[ind] = s
            ind += 1
        ind += d
        for s in cur_p[1]:
            res[ind] = s
            ind += 1
        ind -= 2 * k + d - 1
        if cur == end:
            break
        cur = gr[cur]

    return "".join(res)


for i in range(1, len(a), 1):
    paires.append(a[i].split('|'))

gr = get_pairs(paires)
start = find_start(gr, paires)
end = find_end(gr, paires)
print(get_superstring(start, end, paires, gr))
