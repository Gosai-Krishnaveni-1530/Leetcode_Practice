from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)

        for row, seat in reservedSeats:
            rows[row] |= 1 << (seat-1)

        left = sum(1 << (seat-1) for seat in [2,3,4,5])
        middle = sum(1 << (seat-1) for seat in [4,5,6,7])
        right = sum(1 << (seat-1) for seat in [6,7,8,9])

        answer = 2 * n

        for mask in rows.values():
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            if can_left and can_right:
                continue
            elif can_left or can_middle or can_right:
                answer -= 1
            else:
                answer -= 2
        return answer

