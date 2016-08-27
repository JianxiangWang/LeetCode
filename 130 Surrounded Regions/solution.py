# encoding: utf-8
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if len(board) <= 0:
            return

        m, n = len(board), len(board[0])
        visited = [[False]*n for x in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    surrounded, union_filed = self.bfs(board, i, j, m, n, visited)
                    if surrounded:
                        for x, y in union_filed:
                            board[x][y] = 'X'


    # flood fill, 使用bfs找到union field
    # 判断他是不是被包围, 如果是,返回被包含区域
    def bfs(self, board, x, y, m, n, visited):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        union_filed = []
        surrounded = True

        # 放进queue之前,先visit
        visited[x][y] = True
        for i, j in [(x + d_i, y + d_j) for d_i, d_j in directions]:
            #
            if i < 0 or i >= m or j < 0 or j >= n:
                surrounded = False
                continue
        union_filed.append((x, y))
        queue = [(x, y)]

        while queue:
            i_, j_ = queue.pop(0)

            # 将相邻节点放入queue
            for i, j in [(i_ + d_i, j_ + d_j) for d_i, d_j in directions]:
                #
                if i < 0 or i >= m or j < 0 or j >= n:
                    surrounded = False
                    continue
                if not visited[i][j] and board[i][j] == "O":
                    visited[i][j] = True
                    union_filed.append((i, j))
                    queue.append((i, j))

        return surrounded, union_filed

if __name__ == '__main__':
    board = [
        ["X", "X", "X", "O"],
        ["X", "O", "O", "X"],
        ["X", "O", "X", "O"],
        ["X", "X", "X", "X"]
    ]

    Solution().solve(board)
    print board