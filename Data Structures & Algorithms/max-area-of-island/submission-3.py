class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()
        def dfs(r,c):
            if(r<0 or c<0 or r==ROW or c==COL or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        area = 0
        for i in range(ROW):
            for j in range(COL):
                area = max(area,dfs(i,j))
        return area