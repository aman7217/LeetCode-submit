class Solution:
    def removeOuterParentheses(self, s):
        result = []
        balance = 0

        for ch in s:
            if ch == '(':
                # If balance > 0, this is not the outermost '('
                if balance > 0:
                    result.append(ch)
                balance += 1

            else:
                balance -= 1

                # If balance > 0, this is not the outermost ')'
                if balance > 0:
                    result.append(ch)

        return ''.join(result)