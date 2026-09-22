class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(a, b):
            prod = (a[0] * b[0]) % k
            cnt = a[1][:]

            for r in range(k):
                cnt[(a[0] * r) % k] += b[1][r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                v = value % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans