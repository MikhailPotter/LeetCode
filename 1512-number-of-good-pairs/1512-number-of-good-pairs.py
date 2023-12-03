class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        
        for v in nums:
            if v in hashmap:
                if hashmap[v] == 1:
                    count += 1
                else:
                    count += hashmap[v]
                hashmap[v] += 1
            else:
                hashmap[v] = 1
        return count