from collections import deque
class Solution:
    def numDecodings(self, s: str) -> int:
        decoded = set([str(i) for i in range(1, 27)])
        counts = [0 for i in range(len(s))]
        if len(s) == 1:
            if s == "0":
                return 0
            else:
                return 1
        
        if s[0] in decoded:
            counts[0] += 1
        if s[1] in decoded:
            counts[1] += counts[0]
        if s[0:2] in decoded:
            counts[1] += 1

        for i in range(2, len(s)):
            if s[i] in decoded:
                counts[i] += counts[i-1]
            if s[i-1:i+1] in decoded:
                counts[i] += counts[i-2]
        return counts[-1]

