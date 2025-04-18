class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_count = [(amount + 1)] * (amount + 1)
        min_count[0] = 0

        for count in range(1, len(min_count)):

            for coin in coins:

                if count - coin >= 0 and min_count[count - coin] + 1 < min_count[count]:
                    min_count[count] = min_count[count - coin] + 1

        if min_count[amount] == amount + 1:
            return -1
        return min_count[amount]    
