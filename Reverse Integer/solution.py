
def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    flag = 0
    if x == 0:
        return 0

    if x > 0:
        s = str(x)
    if x < 0:
        flag = 1
        s = str(-x)

    idx = len(s) - 1
    while idx >= 0 and s[idx] == '0':
        idx -= 1

    t = s[:idx + 1][::-1]

    if flag == 0:

        t = int(t)

    else:
        t = -int(t)

    if t > 2 ** 31 -1 or t < - 2 ** 31:
        return 0
    else:
        return t


print reverse(0)

