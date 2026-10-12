class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w2) < len(w1) and w2[:minLength] == w1[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            