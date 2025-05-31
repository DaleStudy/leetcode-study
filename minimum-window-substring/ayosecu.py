from collections import Counter, defaultdict

class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(m), m = len(t)
    """
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_len = len(need)        
        win_dic = defaultdict(int)
        cnt = 0
        min_range, min_len = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            win_dic[c] += 1

            if c in need and win_dic[c] == need[c]:
                cnt += 1

            while cnt == need_len:
                # Update min range
                check_len = r - l + 1
                if check_len < min_len:
                    min_range = [l, r]
                    min_len = check_len

                # Move left pointer
                win_dic[s[l]] -= 1
                if s[l] in need and win_dic[s[l]] < need[s[l]]:
                    cnt -= 1
                l += 1

        return s[min_range[0]:min_range[1]+1] if min_len != float("inf") else ""

tc = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", "")
]

sol = Solution()
for i, (s, t, e) in enumerate(tc, 1):
    r = sol.minWindow(s, t)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
