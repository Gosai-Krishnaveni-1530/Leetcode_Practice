from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odds = [c for c in cnt if cnt[c] % 2 == 1]
        mid = n % 2

        if mid == 0:
            if len(odds) != 0:
                return ""
            oddChar = None
        else:
            if len(odds) != 1:
                return ""
            oddChar = odds[0]

        half = n // 2
        base = [0] * 26
        for c, v in cnt.items():
            base[ord(c) - 97] = v // 2

        # extract target[0..half-1] greedily -> max feasible tie length L
        remaining = base[:]
        L = 0
        for j in range(half):
            idx = ord(target[j]) - 97
            if remaining[idx] > 0:
                remaining[idx] -= 1
                L += 1
            else:
                break

        def back_pass_compare(Tf):
            for t in range(half):
                a = Tf[half - 1 - t]
                b = target[half + mid + t]
                if a > b: return 1
                if a < b: return -1
            return 0

        # Stage 1: front matches target exactly (longest possible tie)
        if L == half:
            Tf = target[0:half]
            ok = False
            if mid == 1:
                if oddChar > target[half]:
                    ok = True
                elif oddChar == target[half]:
                    ok = back_pass_compare(Tf) == 1
            else:
                ok = back_pass_compare(Tf) == 1
            if ok:
                return (Tf + oddChar + Tf[::-1]) if mid == 1 else (Tf + Tf[::-1])

        # Stage 2: deviate at the rightmost feasible position inside the front half
        upper = min(L, half - 1)
        remaining2 = base[:]
        best_i, best_char, best_snapshot = -1, None, None

        for i in range(upper + 1):
            tidx = ord(target[i]) - 97
            found = -1
            for c in range(tidx + 1, 26):
                if remaining2[c] > 0:
                    found = c
                    break
            if found != -1:
                best_i, best_char, best_snapshot = i, found, remaining2[:]
            if i < upper:
                remaining2[ord(target[i]) - 97] -= 1

        if best_i == -1:
            return ""

        H = list(target[0:best_i])
        H.append(chr(best_char + 97))
        rem = best_snapshot[:]
        rem[best_char] -= 1
        for c in range(26):
            if rem[c]:
                H.extend([chr(c + 97)] * rem[c])

        Hs = ''.join(H)
        return (Hs + oddChar + Hs[::-1]) if mid == 1 else (Hs + Hs[::-1])