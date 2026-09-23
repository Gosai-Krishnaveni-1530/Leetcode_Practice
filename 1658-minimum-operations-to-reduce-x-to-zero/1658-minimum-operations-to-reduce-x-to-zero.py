class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        curr = 0
        max_len = -1

        for right in range(len(nums)):
            curr += nums[right]

            while curr > target and left <= right:
                curr -= nums[left]
                left += 1

            if curr == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1