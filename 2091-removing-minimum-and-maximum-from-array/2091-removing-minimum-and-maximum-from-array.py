class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = float("inf")
        maximum = float("-inf")
        min_index = -1
        max_index = -1
        for i in range(n):
            if nums[i] < minimum:
                minimum = nums[i]
                min_index = i

            if nums[i] > maximum:
                maximum = nums[i]
                max_index = i

        left = min(min_index, max_index)
        right = max(min_index, max_index)
        remove_left = right + 1
        remove_right = n - left
        remove_both = (left + 1) + (n - right)

        return min(remove_left, remove_right, remove_both)