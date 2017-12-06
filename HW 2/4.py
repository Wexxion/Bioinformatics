# http://rosalind.info/problems/orf/

import re

dict = {"UUU": 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G',
        }

rg = re.compile(r'(>Rosalind_\d{4})\n([A-Z\n]*)')
good = re.compile(r'(ATG)([A-Z]*?)(TAA|TGA|TAG)')
replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
with open("in.txt", "r") as a:
    a = a.read()
a = rg.findall(a)[0][1].replace('\n', '')
start = 'AUG'
end = ['UAG', 'UGA', 'UAA']


def toRna(s):
    return s.replace("T", "U")


def invert(a):
    replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
    res = ""
    for i in range(len(a)):
        res += replace[a[i]]
    return res


invert_a = invert(a)
a = toRna(a)


def find_start(s, t):
    result = set()
    used = 0
    while True:
        cur = s.find(t)
        if cur == -1:
            break
        result.add(cur + used)
        s = s[1::]
        used += 1
    return result


def find_seq(st):
    end = ['UAG', 'UGA', 'UAA']
    cur_s = ''
    for i in range(0, len(st), 3):
        cur = st[i:i + 3]
        if cur not in end:
            cur_s += dict[cur]
        elif cur in end:
            if cur_s != '':
                return cur_s


start_ind = find_start(a, start)
res = set()
for i in start_ind:
    res.add(find_seq(a[i:]))
start_ind = find_start(toRna(invert_a[::-1]), 'AUG')
for i in start_ind:
    res.add(find_seq(toRna(invert_a[::-1])[i:]))
for i in res:
    if i:
        print(i)
