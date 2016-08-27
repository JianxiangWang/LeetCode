# encoding: utf-8

# dp[i] 表示以i结尾的子数组的最大和,
# 那么, if dp[i] - 1 <= 0: dp[i] = array[i]
# if dp[i-1] > 0: dp[i] = dp[i-1] + array[i]
def findMaxSubArray(array):

    dp = [None] * len(array)
    for idx in range(0, len(array)):
        if idx == 0 or dp[idx - 1] <= 0:
            dp[idx] = array[idx]
        else:
            dp[idx] = dp[idx - 1] + array[idx]

    print max(dp)

if __name__ == '__main__':
    array = [1, -2, 3, 10, -4, 7, 2, -5]

    findMaxSubArray(array=array)
