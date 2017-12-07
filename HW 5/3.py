# http://rosalind.info/problems/ba5m/

from pprint import pprint


def get_input():
    with open('in.txt') as file:
        a, b, c = file.readlines()
    return a.strip(), b.strip(), c.strip()


def create_array(default, a, b, c):
    return [[[default for _1 in range(a)] for _2 in range(b)] for _3 in range(c)]


def get_matrix(a, b, c):
    traceback = create_array(None, len(a) + 1, len(b) + 1, len(c) + 1)
    res = create_array(0, len(a) + 1, len(b) + 1, len(c) + 1)

    def val(x, y, z, dx=0, dy=0, dz=0, d=0):
        if x + dx < 0 or y + dy < 0 or z + dz < 0:
            return
        value = res[x + dx][y + dy][z + dz] + d
        if value > res[x][y][z]:
            res[x][y][z] = value
            traceback[x][y][z] = (x + dx, y + dy, z + dz)

    for x in range(len(a)):
        for y in range(len(b)):
            for z in range(len(c)):
                val(x, y, z, dx=-1)
                val(x, y, z, dy=-1)
                val(x, y, z, dz=-1)
                if a[x] == b[y] == c[z]:
                    val(x, y, z, dx=-1, dy=-1, dz=-1, d=1)

    return res, traceback


def get_path(current, tr, a, b, c):
    res1 = ''
    res2 = ''
    res3 = ''
    while current != (0, 0, 0):
        previous = tr[current[0]][current[1]][current[2]]
        current = previous
    return res1[::-1], res2[::-1], res3[::-1]


if __name__ == '__main__':
    a, b, c = get_input()
    matrix, tr = get_matrix(a, b, c)
    # pprint(matrix)

    maximum = matrix[-1][-1][-1]
    last = len(matrix) - 1, len(matrix[0]) - 1, len(matrix[0][0]) - 1

    a, b, c = get_path(last, tr, a, b, c)
    print(maximum)
    print(a)
    print(b)
    print(c)
