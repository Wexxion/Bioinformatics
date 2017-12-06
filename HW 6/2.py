# http://rosalind.info/problems/ba10b/

def get_input():
    with open('in.txt') as file:
        path1 = file.readline().strip()
        file.readline()
        varbs1 = file.readline().split()
        file.readline()
        path2 = file.readline().strip()
        file.readline()
        varbs2 = file.readline().split()
        file.readline()
        file.readline()

        vdict = {}
        matrix = [[0] * len(varbs1) for _ in range(len(varbs2))]

        for i in range(len(varbs1)):
            vdict[varbs1[i]] = i
            sp = file.readline().split()[1:]
            for j in range(len(sp)):
                matrix[i][j] = float(sp[j])
        for i in range(len(varbs2)):
            vdict[varbs2[i]] = i
    return path1, path2, vdict, matrix


if __name__ == '__main__':
    path1, path2, vdict, matrix = get_input()
    res = 1
    for i in range(len(path1)):
        res *= matrix[vdict[path2[i]]][vdict[path1[i]]]


    print(res)

