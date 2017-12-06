# http://rosalind.info/problems/ba5j/

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


def get_matrix(s1, s2, d=-11, e=-1):
    traceback = [[None for _1 in range(len(s2) + 1)] for _2 in range(len(s1) + 1)]
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
            if match > res[i][j]:
                res[i][j] = match
                traceback[i][j] = (i - 1, j - 1)

            for k in range(1, len(s1) + 1):
                if k <= i:
                    new_match = res[i - k][j] + d + e * (k - 1)
                    if new_match > res[i][j]:
                        res[i][j] = new_match
                        traceback[i][j] = (i - k, j)

            for k in range(1, len(s2) + 1):
                if k <= i:
                    new_match = res[i][j - k] + d + e * (k - 1)
                    if new_match > res[i][j]:
                        res[i][j] = new_match
                        traceback[i][j] = (i, j - k)

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


def get_path(current, tr, s1, s2):
    res1 = ''
    res2 = ''
    while current != (0, 0):
        previous = tr[current[0]][current[1]]
        if current[0] - previous[0] == 1 and current[1] - previous[1] == 1:
            res1 += s1[previous[0]]
            res2 += s2[previous[1]]
        elif current[0] - previous[0] == 1:
            res1 += s1[previous[0]]
            res2 += '-'
        elif current[1] - previous[1] == 1:
            res1 += '-'
            res2 += s2[previous[1]]
        else:
            if current[0] - previous[0] > 1:
                d = current[0] - previous[0]
                temp = ''
                for i in range(d):
                    temp += s1[previous[0] + i]
                    res2 += '-'
                res1 += temp[::-1]
            else:
                d = current[1] - previous[1]
                temp = ''
                for i in range(d):
                    res1 += '-'
                    temp += s2[previous[1] + i]
                res2 += temp[::-1]

        current = previous
    return res1[::-1], res2[::-1]


if __name__ == '__main__':
    s1, s2 = open("in.txt").readlines()
    n = max([len(s1), len(s2)])
    s1, s2 = s1.strip(), s2.strip()
    matrix, tr = get_matrix(s1, s2)
    maximum = matrix[-1][-1]
    last = len(matrix) - 1, len(matrix[0]) - 1
    a, b = get_path(last, tr, s1, s2)
    print(maximum)
    print(a)
    print(b)
