class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c] == 1):
                    fresh += 1
                if(grid[r][c] == 2):
                    q.append((r, c))
        def bfs(r, c, q):
            nonlocal fresh
            if(r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append((r, c))
            fresh -= 1
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r+1, c, q)
                bfs(r, c+1, q)
                bfs(r-1, c, q)
                bfs(r, c-1, q)
            time += 1
        return time if fresh == 0 else -1






















        # q = deque()
        # fresh = 0
        # ROWS, COL = len(grid), len(grid[0])
        # for i in range(ROWS):
        #     for j in range(COL):
        #         if grid[i][j] == 1:
        #             fresh += 1
        #         if grid[i][j] == 2:
        #             q.append([i, j])
        # def bfs(i, j, grid):
        #     nonlocal fresh
        #     if(i < 0 or j < 0 or i == ROWS or j == COL or grid[i][j] != 1):
        #         return
        #     grid[i][j] = 2
        #     q.append([i, j])
        #     fresh -= 1
        # time = 0
        # while q and fresh: #while there is a queue of rotten oranges which can spread, and fresh oranges that are yet to be infected
        #     for i in range(len(q)): # process rotten oranges at time t
        #         i, j = q.popleft()
        #         bfs(i+1, j, grid)
        #         bfs(i-1, j, grid)
        #         bfs(i, j+1, grid)
        #         bfs(i, j-1, grid)
        #     time += 1 
        # return time if fresh == 0 else -1

        