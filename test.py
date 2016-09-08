import sys


def solve():
    T = int(raw_input())
    while T > 0:
        n = int(raw_input())

        print helper(int(n))

        T -= 1


def helper(n):
    c = 0

    for i in range(1, n + 1):
        # 10
        s = 0
        for x in str(i):
            s += int(x)
        # 2
        t = 0
        for x in bin(i)[2:]:
            t += int(x)
        if s == t:
            c += 1

    return c


if __name__ == '__main__':
    import math

    print 1/15.0 * math.log(9/15.) + 1/10.0 * math.log(9/10.0) + 1/6.0 * math.log(9/6.)
