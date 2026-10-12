class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stoneOne, stoneTwo = stones.pop(), stones.pop()
            if abs(stoneOne-stoneTwo) > 0:
                stones.append(abs(stoneOne-stoneTwo))
        return 0 if len(stones) == 0 else stones[0]
        