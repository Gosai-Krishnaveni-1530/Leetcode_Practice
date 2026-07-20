from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Effective shifts
        k %= (m * n)

        # Rotate
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D
        ans = []
        idx = 0
        for i in range(m):
            ans.append(arr[idx:idx + n])
            idx += n

        return ans