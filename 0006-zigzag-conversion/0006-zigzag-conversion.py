class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = -1
        j = 0
        moving = numRows
        temp = []
        while j < len(s):
            if j < numRows:
                temp.append([s[j]])
            else:
                moving += i
                if moving == numRows or moving <= 1:
                     i = -i
                temp[moving - 1].append(s[j])
            j += 1

        word = ""
        for t in temp:
            word += "".join(t)
        return word