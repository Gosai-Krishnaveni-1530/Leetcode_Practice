class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')
        
            if count[t] > 0:
                ans.append(target[i])
                count[t] -= 1
            else:
                for c in range(t + 1, 26):
                    if count[c] > 0:
                        ans.append(chr(c + ord('a')))
                        count[c] -= 1
                        
                        for x in range(26):
                            ans.extend(chr(x + ord('a')) * count[x])
                        
                        return ''.join(ans)
                    

                break

        for i in range(len(ans) - 1, -1, -1):
            c = ord(ans[i]) - ord('a')
            count[c] += 1

            for bigger in range(c + 1, 26):
                if count[bigger] > 0:
                    result = ans[:i] + [chr(bigger + ord('a'))]
                    count[bigger] -= 1

                    for x in range(26):
                        result.extend(chr(x + ord('a')) * count[x])
                    
                    return ''.join(result)
        return ""