class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        symbols = "!?',;."
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')
        words = paragraph.lower().split()
        
        counter = dict()
        for w in words:
            if w in banned:
                continue
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1

        freq_w, max = '', 0
        for w, f in counter.items():
            if f > max:
                max = f
                freq_w = w
        return freq_w