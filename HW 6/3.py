# http://rosalind.info/problems/ba10c/
import numpy as np


def get_input():
    with open('in.txt') as file:
        string = file.readline().strip()

        file.readline()
        alph = {s: i for (i, s) in enumerate(file.readline().split())}

        file.readline()
        states = {i: s for (i, s) in enumerate(file.readline().split())}

        file.readline()
        file.readline()
        transition = [[0] * len(states) for _ in range(len(states))]
        for i in range(len(states)):
            sp = file.readline().split()[1:]
            for j in range(len(sp)):
                transition[i][j] = float(sp[j])

        file.readline()
        file.readline()
        emission = [[0] * len(alph) for _ in range(len(states))]
        for i in range(len(states)):
            sp = file.readline().split()[1:]
            for j in range(len(sp)):
                emission[i][j] = float(sp[j])

    return string, alph, states, np.array(emission), np.array(transition)


def viterbi(string, alph, states, emission, transition):
    def log(l, k, i):
        si = alph[string[i]]
        return np.log(emission[k, si] * transition[l, k])

    score = np.empty(shape=(len(states), len(string)), dtype=float)
    traceback = np.zeros(shape=(len(states), len(string)), dtype=int)

    score[:, 0] = np.log(1 / len(states) * emission[:, alph[string[0]]])
    for i in range(1, len(string)):
        for k in range(len(states)):
            curr_score = np.array(list(map(lambda l: score[l, i - 1] + log(l, k, i), range(len(states)))))
            score[k, i] = curr_score.max()
            traceback[k, i] = curr_score.argmax()

    rpath = []
    state = score[:, len(string) - 1].argmax()
    rpath.append(states[state])
    for i in range(len(string) - 1, 0, -1):
        state = traceback[state, i]
        rpath.append(states[state])
    return ''.join(rpath[::-1])


if __name__ == '__main__':
    print(viterbi(*get_input()))
