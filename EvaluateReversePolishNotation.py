class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if (token[0] == '-' and len(token) > 1) or token.isnumeric():
                result.append(int(token))
            else:
                num2 = result.pop()
                num1 = result.pop()
                if token == '+':
                    ans = num1 + num2
                elif token == '-':
                    ans = num1 - num2
                elif token == '*':
                    ans = num1 * num2
                elif token == '/':
                    ans = int(num1 / num2)
                result.append(ans)
        return result[0]
