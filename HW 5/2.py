# http://rosalind.info/problems/cons/


with open('in.txt') as file:
    data = file.readlines()
    res = []
    string = ''
    letters = {'A': [0], 'C': [0], 'G': [0], 'T': [0]}
    for i in range(1, len(data), 2):
        res.append(data[i].strip())

    for i in range(len(res[0])):
        for dna in res:
            letters[dna[i]][-1] += 1

        maxi = 0
        for key in letters.keys():
            if letters[key][i] >= maxi:
                maxi = letters[key][i]
                char = key

            if i != len(res[0]) - 1:
                letters[key].append(0)
        string += char

    print(string)
    print('A:', ' '.join(str(i) for i in letters['A']))
    print('C:', ' '.join(str(i) for i in letters['C']))
    print('G:', ' '.join(str(i) for i in letters['G']))
    print('T:', ' '.join(str(i) for i in letters['T']))



