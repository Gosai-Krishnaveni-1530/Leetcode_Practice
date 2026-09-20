class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(0,len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            mul = value * (i+1)
            sum = sum+mul
        return sum