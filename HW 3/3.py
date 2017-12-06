# http://rosalind.info/problems/corr/


import re
from collections import Counter

rg = re.compile(r'>Rosalind_\d{4}\n([A-Z\n]*)')
with open("in.txt", "r") as a:
    a = a.read()


def hamming_dist(a, b):
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    return res


def invert(a):
    replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
    res = ""
    for i in range(len(a)):
        res += replace[a[i]]
    return res


a = [x.replace('\n', '') for x in rg.findall(a)]
b = [invert(x)[::-1] for x in a]
res = []
counter = Counter(a)
bad = []
good = []
for x in counter:
    if counter[x] >= 2:
        good.append(x)
for x in counter:
    if counter[x] == 1 and x not in b:
        bad.append(x)
for x in bad:
    for y in good + b:
        if hamming_dist(x, y) == 1:
            res.append((x, y))
            break
for x in res:
    print("->".join(x))
