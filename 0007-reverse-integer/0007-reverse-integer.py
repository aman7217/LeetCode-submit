class Solution:
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:
            digit = x % 10
            x //= 10

            # Check overflow before rev * 10 + digit
            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev

