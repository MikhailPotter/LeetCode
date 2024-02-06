class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        curr_stack = [prev]
        result = 0
        for price in prices[1:]:
            if price < prev:
                result += curr_stack[-1] - curr_stack[0]
                curr_stack = [price]
            else:
                curr_stack.append(price)                
            prev = price 
        result += curr_stack[-1] - curr_stack[0]
        return result