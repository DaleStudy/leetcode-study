class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(s)
        if n == 0:
            return 0

        count = 0

        for i in range(n):
            # 중심이 하나(홀수 길이 회문)
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # 중심이 둘 사이(짝수 길이 회문)
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
