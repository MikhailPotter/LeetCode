class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while True:
            tickets[0] -= 1
            time += 1
            first_man = tickets[0]
            tickets.pop(0)
            if first_man:
                tickets.append(first_man)
            elif k == 0:
                break
            if k == 0:
                k = len(tickets) - 1
            else:
                k -= 1
        return time

        