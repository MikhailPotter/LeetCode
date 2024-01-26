class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res, prev_lsr, curr_lsr = 0, 0, bank[0].count('1')
        for i in range(1, len(bank)):
            curr = bank[i].count('1')
            if curr == 0:
                continue
            prev_lsr, curr_lsr = curr_lsr, curr
            res += prev_lsr * curr_lsr
        return res