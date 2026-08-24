class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = 0
        prefixes = []

        for x in stones:
            prefix += x
            prefixes.append(prefix)
        
        best = prefixes[-1]

        for i in range(len(stones) - 2, 0, -1):
            best = max(best, prefixes[i] - best)
        
        return best