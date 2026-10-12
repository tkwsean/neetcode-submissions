class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        ROWS, COL = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        def bfs(i, j, grid):
            nonlocal fresh
            if(i < 0 or j < 0 or i == ROWS or j == COL or grid[i][j] != 1):
                return
            grid[i][j] = 2
            q.append([i, j])
            fresh -= 1
        time = 0
        while q and fresh:
            for i in range(len(q)):
                i, j = q.popleft()
                bfs(i+1, j, grid)
                bfs(i-1, j, grid)
                bfs(i, j+1, grid)
                bfs(i, j-1, grid)
            time += 1 
        return time if fresh == 0 else -1

        