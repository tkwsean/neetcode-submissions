class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for nei in adjList[curr]:
                    dfs(nei)
        numConnected = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                numConnected += 1
        return numConnected
        