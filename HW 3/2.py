import re
import math

rg = re.compile(r'>Rosalind_\d{4}\n([A-Z\n]*)')

with open("in.txt", "r") as a:
    a = a.read()

a = [x.replace('\n', '') for x in rg.findall(a)]


def find_match_end(s1, s2):
    n = min(len(s1), len(s2))
    for i in range(n - 1, 0, -1):
        if s1[-i:] == s2[:i] and 2 * i > len(s2) and 2 * i > len(s1):
            return i


def find_pare(a):
    res = {}
    for x in range(len(a)):
        for y in range(len(a)):
            if x != y:
                ind = find_match_end(a[x], a[y])
                if ind:
                    res[x] = y
    return res


def create_graph():
    gr = {}
    n = len(a)
    for x in a:
        gr[x] = []
    for i in range(n):
        for j in range(n):
            if i != j:
                ind = find_match_end(a[i], a[j])
                if ind:
                    gr[a[i]].append(a[j])
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


def get_superstring(start, end, paires):
    res = a[start]
    cur = start
    while cur != end:
        cur_s = a[cur]
        cur = pares[cur]
        next_s = a[cur]
        ind = find_match_end(cur_s, next_s)
        res += next_s[ind:]
    return res


pares = find_pare(a)
start = find_start(pares, a)
end = find_end(pares, a)
print(get_superstring(start, end, pares))
