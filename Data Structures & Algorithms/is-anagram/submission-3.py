class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorts = sorted(s)
        sortt = sorted(t)
        return sorts == sortt