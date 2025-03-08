class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        numbers = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                numbers.append(int(t))
            else:
                if t == '/':
                    a = int(numbers[-2] / numbers[-1])
                elif t == '+':
                    a = numbers[-2] + numbers[-1]
                elif t == '*':
                    a = numbers[-2] * numbers[-1]
                elif t == '-':
                    a = numbers[-2] - numbers[-1]
                numbers.pop()
                numbers.pop()
                numbers.append(a)
        return numbers[0]