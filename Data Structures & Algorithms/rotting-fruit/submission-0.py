class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        def bfs(r, c, grid):
            nonlocal fresh
            if(r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1):
                return
            grid[r][c] = 2
            fresh -= 1 
            q.append([r, c])
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r+1, c, grid)
                bfs(r-1, c, grid)
                bfs(r, c+1, grid)
                bfs(r, c-1, grid)
            time += 1
        return time if fresh == 0 else -1
        