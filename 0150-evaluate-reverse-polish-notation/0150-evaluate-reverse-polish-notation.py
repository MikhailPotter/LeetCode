import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }
        
        for token in tokens:
            if token in ops.keys():
                second = stack[-1]
                stack.pop()
                first = stack[-1]
                stack.pop()
                res = math.trunc(ops[token](first, second))
                stack.append(res)
                print(res, first, second)
            else:
                stack.append(int(token))
        return stack[-1]