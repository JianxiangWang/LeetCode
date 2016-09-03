import copy




def solve(A, B, N, K):

    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            s = i**A + j**B
            if s % K == 0:
                ans += 1

    return ans



if __name__ == '__main__':


