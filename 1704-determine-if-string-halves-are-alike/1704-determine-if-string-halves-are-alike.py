class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s, l = s.lower(), len(s)
        return len(re.findall("[aeiou]", s[:l // 2])) == len(re.findall("[aeiou]", s[l // 2:]))