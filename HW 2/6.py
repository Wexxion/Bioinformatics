# http://rosalind.info/problems/grph/

import re

rg = re.compile(r'>(Rosalind_\d{4})\n([A-Z\n]*)')
with open("in.txt", "r") as a:
    a = a.read()
a = rg.findall(a)
res = set()
for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            if a[i][1][:3] == a[j][1].strip()[-3:]:
                res.add((a[j][0], a[i][0]))
for x in res:
    print(" ".join(x))
