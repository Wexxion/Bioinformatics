# http://rosalind.info/problems/fib/


def fib(old, young, rate, months):
    if months == 1:
        result = young
    else:
        result = fib(young, old * rate + young, rate, months - 1)
    return result


with open('in.txt') as file:
    months, rate = map(int, file.read().split())
    print(fib(0, 1, rate, months))
