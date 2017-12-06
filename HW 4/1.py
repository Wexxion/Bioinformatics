# http://rosalind.info/problems/ba5g/


def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i, c2 in enumerate(s2):
        distances_ = [i+1]
        for j, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[j])
            else:
                distances_.append(1 + min((distances[j], distances[j + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


if __name__ == '__main__':
    s1, s2 = input(), input()
    print(levenshtein_distance(s1, s2))
