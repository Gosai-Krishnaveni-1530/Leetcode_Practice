class Solution:
    def uniformArray(self, nums1):
        mn = min((x for x in nums1 if x % 2), default=None)
        return mn is None or all(x >= mn for x in nums1 if x % 2 == 0)