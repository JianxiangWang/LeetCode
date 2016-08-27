# encoding: utf-8

# 11000
# 11000
# 00100
# 00011
# Answer: 3


# flood fill and bfs
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for x in range(m) ]

        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, x, y, m, n, visited)

        return ans


    def bfs(self, grid, x, y, m, n, visited):

        # 4个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 以 (x, y) 为起点, 沿着四个方向, 把能访问的全部visit掉!
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            curr_point = queue.pop(0)

            # 把有效的节点, 入队
            for h, v in directions:
                this_x, this_y = curr_point[0] + h, curr_point[1] + v
                if this_x >= 0 and this_x < m and this_y >= 0 and this_y < n \
                        and not visited[this_x][this_y] and grid[this_x][this_y] == "1":
                    visited[this_x][this_y] = True
                    queue.append((this_x, this_y))



if __name__ == '__main__':
    grid = ["11110", "11010", "11000", "00000"]

    print Solution().numIslands(grid)
