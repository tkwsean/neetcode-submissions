class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited, q = set(), deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append([i, j])
        def bfs(i, j, grid):
            if(i < 0 or j < 0 or i == ROWS or j == COLS or grid[i][j] == -1 or (i, j) in visited):
                return
            visited.add((i, j))
            q.append([i, j])
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                bfs(r+1, c, grid)
                bfs(r-1, c, grid)
                bfs(r, c+1, grid)
                bfs(r, c-1, grid)
            distance += 1 