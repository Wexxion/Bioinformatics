# http://rosalind.info/problems/gc/

import re

a = open("bio.txt", "r")
a = a.read()

rg = re.compile(r'(>Rosalind_\d{4})\n([A-Z\n]*)')
parts = rg.findall(a)
res = {}
print(parts)


def count(st):
    return (st.count("C") + st.count("G")) / len(st)


for elems in parts:
    res.update([(elems[0][1:], count(elems[1].replace("\n", "")))])

max = 0
res_key = ""
for key in res:
    if res[key] > max:
        max = res[key]
        res_key = key
print(res_key, max * 100)
