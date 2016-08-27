#encoding: utf-8
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        visited  = [[False] * n for _ in range(m)]

        # 使用堆 ~
        heap = [(matrix[0][0], 0, 0)]
        visited[0][0] = True
        ans = None
        for _ in range(k):
            val, i, j = heapq.heappop(heap)
            directions = [(0, 1), (1, 0)]
            for d_i, d_j in directions:
                if (i+d_i) < m and (j+d_j) < n and not visited[i+d_i][j+d_j]:
                    heapq.heappush(heap, (matrix[i+d_i][j+d_j], i+d_i, j+d_j))
                    visited[i + d_i][j + d_j] = True
            ans = val

        return ans


if __name__ == '__main__':
    matrix = [
       [ 1,  5.555,  9],
       [10, 11, 13],
       [12, 13, 1000]
    ]
    k = 8
    print Solution().kthSmallest(matrix, k)
