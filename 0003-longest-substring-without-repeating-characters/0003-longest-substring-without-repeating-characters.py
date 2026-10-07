class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            
            visited.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length