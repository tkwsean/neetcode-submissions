class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freqCounter = Counter(hand)
        hand.sort()
        for num in hand:
            if freqCounter[num]:
                for i in range(num, num+groupSize):
                    if not freqCounter[i]:
                        return False
                    freqCounter[i] -= 1
        return True 