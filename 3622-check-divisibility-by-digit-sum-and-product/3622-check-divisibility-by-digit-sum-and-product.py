class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digits = []
        add = 0
        product = 1
        while temp>0:
            digit = temp % 10
            digits.append(digit)
            temp = temp // 10
        for i in digits:
            add += i
            product *= i
        result = add + product 
        if n % result == 0:
            return True
        
        return False
