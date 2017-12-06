# http://rosalind.info/problems/ba10a/


def get_input():
    with open('in.txt') as file:
        path = file.readline().strip()
        file.readline()
        varbs = file.readline().split()
        file.readline()
        file.readline()

        vdict = {}
        matrix = [[0] * len(varbs) for _ in range(len(varbs))]
        for i in range(len(varbs)):
            vdict[varbs[i]] = i
            sp = file.readline().split()[1:]
            for j in range(len(sp)):
                matrix[i][j] = float(sp[j])
    return path, varbs, vdict, matrix


if __name__ == '__main__':
    path, varbs, vdict, matrix = get_input()
    pairs = [path[i:i + len(varbs)] for i in range(0, len(path))]
    res = 1
    for pair in pairs[:-1]:
        res *= matrix[vdict[pair[0]]][vdict[pair[1]]]
    print(res / 2)
