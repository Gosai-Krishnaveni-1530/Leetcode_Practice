class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted(range(n), key=lambda i: nums[i])
        
        result = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[pairs[j + 1]] - nums[pairs[j]] <= limit:
                j += 1
            group_indices = sorted(pairs[i:j+1])
            group_values = [nums[pairs[k]] for k in range(i, j+1)]
            
            for idx, val in zip(group_indices, group_values):
                result[idx] = val
            
            i = j + 1
        
        return result