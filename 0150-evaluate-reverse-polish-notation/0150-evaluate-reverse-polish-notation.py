class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ops = set(['+', '-', '*', '/'])
        
        for token in tokens:
            if token in ops:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '*':
                    stack.append(first * second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '/':
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack.pop()