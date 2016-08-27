

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    T = set(["a","e","i","o","u"])

    s = list(s)
    L = 0
    R = len(s) - 1

    while L < len(s):
        if s[L].lower() in T:
            break
        L += 1

    while R >= 0:
        if s[R].lower() in T:
            break
        R -= 1

    while L < R:
        s[L], s[R] = s[R], s[L]

        L += 1
        while L < len(s):
            if s[L].lower() in T:
                break
            L += 1

        R -= 1
        while R >= 0:
            if s[R].lower() in T:
                break
            R -= 1

    return "".join(s)


print reverseVowels("hello")
