class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        isSorted = sorted(stones, reverse=True)
        while len(isSorted) > 0:
            if len(isSorted) == 1:
                return isSorted[0]
            first, second = isSorted[0], isSorted[1]
            if first == second:
                isSorted.pop(0)
                isSorted.pop(0)
                isSorted.sort(reverse=True)
            elif first > second:
                isSorted.pop(1)
                isSorted[0] = isSorted[0] - second
                isSorted.sort(reverse=True)
            elif first < second:
                isSorted.pop(0)
                isSorted[0] = isSorted[0] - first
                isSorted.sort(reverse=True)
        return isSorted[0] if len(isSorted) == 1 else 0
                