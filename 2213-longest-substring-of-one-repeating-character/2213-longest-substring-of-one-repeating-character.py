class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        n = len(s)

        # Node:
        # (left_char, right_char, prefix, suffix, best, length)
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            lc, lr, lp, ls, lb, llen = left
            rc, rr, rp, rs, rb, rlen = right

            # Boundary characters are equal:
            can_merge = lr == rc

            prefix = lp
            if lp == llen and can_merge:
                prefix = llen + rp

            suffix = rs
            if rs == rlen and can_merge:
                suffix = rlen + ls

            best = max(lb, rb)

            if can_merge:
                best = max(best, ls + rp)

            return (
                lc,
                rr,
                prefix,
                suffix,
                best,
                llen + rlen
            )

        def build(node, left, right):
            if left == right:
                tree[node] = (
                    s[left],  # left_char
                    s[left],  # right_char
                    1,        # prefix
                    1,        # suffix
                    1,        # best
                    1         # length
                )
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans