class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        parity_count = [1, 0]
        result = 0
        prefix_sum = 0
      
        for num in arr:
            prefix_sum += num
            current_parity = prefix_sum & 1
            opposite_parity = current_parity ^ 1
            result = (result + parity_count[opposite_parity]) % MOD
            parity_count[current_parity] += 1
      
        return result