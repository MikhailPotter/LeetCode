class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        climb_cost = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(climb_cost)):
            climb_cost[i] = min(climb_cost[i - 1] + cost[i - 1], climb_cost[i - 2] + cost[i - 2])
        return climb_cost[-1]