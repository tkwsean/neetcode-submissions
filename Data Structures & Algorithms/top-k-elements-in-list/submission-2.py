import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        result = []
        while(len(result) < k):
            result.append(heapq.heappop(heap)[1])
        return result