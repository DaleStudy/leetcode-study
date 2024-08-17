class Solution:
    # Time complexity: O(n^2) = O(n) * O(n)
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        n = len(s)

        def two_pointer_expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        for i in range(0, n):
            # 1, 3, 5 ...
            two_pointer_expand(i, i)
            # 2, 4, 6 ...
            two_pointer_expand(i, i + 1)

        return self.count