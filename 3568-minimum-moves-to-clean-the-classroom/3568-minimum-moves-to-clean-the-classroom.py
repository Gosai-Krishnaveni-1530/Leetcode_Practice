from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        n, m = len(classroom), len(classroom[0])

        litter = []
        sr = sc = 0

        for r in range(n):
            for c in range(m):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter.append((r, c))

        k = len(litter)

        if k == 0:
            return 0

        litter_id = {pos: i for i, pos in enumerate(litter)}
        full = (1 << k) - 1

        states = 1 << k
        best = [-1] * (n * m * states)

        start = (sr * m + sc) * states
        best[start] = energy

        q = deque([(sr, sc, 0, energy, 0)])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            r, c, mask, e, moves = q.popleft()

            if mask == full:
                return moves

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                cell = classroom[nr][nc]

                if cell == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                idx = litter_id.get((nr, nc))
                if idx is not None:
                    nmask |= 1 << idx

                if cell == 'R':
                    ne = energy

                state_idx = ((nr * m + nc) * states) + nmask

                if ne <= best[state_idx]:
                    continue

                best[state_idx] = ne
                q.append((nr, nc, nmask, ne, moves + 1))

        return -1