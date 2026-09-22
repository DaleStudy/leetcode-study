class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        success = set([(i, i + 1) for i in range(s_len)])

        for r in range(s_len):
            for l in range(0, r):
                if r - l == 1 and s[l] == s[r]:
                    success.add((l, r + 1))
                    continue

                if (l + 1, r) in success and s[l] == s[r]:
                    success.add((l, r + 1))

        return len(success)
