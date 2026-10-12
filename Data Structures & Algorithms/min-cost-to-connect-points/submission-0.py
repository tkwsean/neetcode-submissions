import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        res = 0
        visited = set()
        minHeap = [[0, 0]]
        while len(visited) < n:
            dist, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)
            res += dist
            for cost, nei in adj[currNode]:
                if nei not in visited:
                    heapq.heappush(minHeap, (cost, nei))
        return res 