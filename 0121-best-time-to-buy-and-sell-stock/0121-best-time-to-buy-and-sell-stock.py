class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_buy = -1
        cur_sell = 0
        profit = 0

        for price in prices:
            if cur_buy == -1:
                cur_buy = price
                cur_sell = price
            elif cur_buy > price:
                if cur_sell - cur_buy > profit:
                    profit = cur_sell - cur_buy
                cur_buy = price
                cur_sell = price
            elif cur_sell < price:
                cur_sell = price
        if cur_sell - cur_buy > profit:
            profit = cur_sell - cur_buy
        return profit



        