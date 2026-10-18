class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        def add(t, r, c):
            if r < 0 or c < 0 or r == N or c == N or (r, c) in visited:
                return
            visited.add((r, c))
            heapq.heappush(minHeap, (max(t, grid[r][c]), r, c))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return t
            add(t, r+1, c)
            add(t, r, c+1)
            add(t, r-1, c)
            add(t, r, c-1)
            