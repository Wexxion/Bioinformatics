# http://rosalind.info/problems/revc/

a = input()
a = a[::-1]
replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
res = ""
for i in range(len(a)):
    res += replace[a[i]]

print(res)
