from pprint import pprint


def get_input():
    with open('in.txt') as file:
        path = file.readline().strip()

        file.readline()
        alph = file.readline().split()

        file.readline()
        states = file.readline().split()

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

        print(emission)
    return path, states, emission, transition


if __name__ == '__main__':
    path, states, emission, transition = get_input()