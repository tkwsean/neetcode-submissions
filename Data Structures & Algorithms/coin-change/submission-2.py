class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [999]*(amount+1)
        dp[0] = 0
        for currAmount in range(1, amount+1):
            for coin in coins:
                if currAmount - coin >= 0:
                    dp[currAmount] = min(dp[currAmount], dp[currAmount-coin]+1)
        return dp[amount] if dp[amount] != 999 else -1