class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
    
        res = [0] * (n+1)
        res[1] = 1

        block = 2
        cur_block = 0
        for i in range(2, n+1):
            res[i] = 1 + res[cur_block]
            cur_block += 1

            if cur_block == block:
                block *= 2
                cur_block = 0
        return(res)
