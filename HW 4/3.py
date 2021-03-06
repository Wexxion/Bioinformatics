# http://rosalind.info/problems/ba5k/

blosum = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
          [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
          [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
          [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
          [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
          [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
          [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
          [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
          [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
          [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
          [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
          [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
          [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
          [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
          [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
          [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
          [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
          [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
          [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
          [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]
letters = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8,
           'L': 9, 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}


def get_matrix(s1, s2, d=-5):
    traceback =  [[None for _1 in range(len(s2) + 1)] for _2 in range(len(s1) + 1)]
    res = [[-100 ** 7 for _1 in range(len(s2) + 1)] for _2 in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        res[i][0] = d * i
        traceback[i][0] = (i - 1, 0)
    for j in range(len(s2) + 1):
        res[0][j] = d * j
        traceback[0][j] = (0, j - 1)

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            match = res[i - 1][j - 1] + blosum[letters[s1[i - 1]]][letters[s2[j - 1]]]
            delete = res[i - 1][j] + d
            insert = res[i][j - 1] + d
            res[i][j] = max(match, delete, insert)

            if res[i][j] == match:
                traceback[i][j] = (i - 1, j - 1)
            elif res[i][j] == delete:
                traceback[i][j] = (i - 1, j)
            else:
                traceback[i][j] = (i, j - 1)

    return res, traceback


def print_matrix(matrix):
    count1 = 0
    print(' [i,j]', end='')
    for i in range(len(matrix[0])):
        print('[{}]'.format(i).rjust(4, ' '), end=' ')
    print()
    for i in matrix:
        print('[{}]'.format(count1).rjust(4, ' '), end=' ')
        for j in i:
            print(str(j).rjust(4, ' '), end=' ')
        print()
        count1 += 1


def get_path(current, tr):
    res = []
    while current != (0, 0):
        previous = tr[current[0]][current[1]]
        res.append(previous)
        current = previous
    return res


if __name__ == '__main__':
    s1, s2 = open("in.txt").readlines()
    n = max([len(s1), len(s2)])
    matrix, tr = get_matrix(s1.strip(), s2.strip())
    # print_matrix(matrix)
    maximum = matrix[-1][-1]
    last = len(matrix) - 1, len(matrix[0]) - 1
    print(maximum)
    res = get_path(last, tr)
    for i in range(len(s2)):
        if len(s2) // 2 in res[i]:
            print(res[i], res[i-1])
            break
    # a = len(res)
    # print(a)
    # print(len(s1) // 2)
    # print(len(s2) // 2)
    # if a % 2 == 0:
    #     b = a // 2 + 1
    # else:
    #     b = a // 2 - 1
    # print(res[b - 1], res[b - 2])