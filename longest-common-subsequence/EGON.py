from unittest import TestCase, main


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve_dp(text1, text2)

    """
    Runtime: 441 ms (Beats 85.60%)
    Time Complexity: O(m * n)
        - text1, text2의 길이를 각각 m, n이라 하면 이중 for문 조회에 O(m * n)
        - i. dp 배열 값 갱신에서 기존값 +1에 O(1)
        - ii. dp 배열 값 갱신에서 2개 항에 대한 max 연산에 O(2), upper bound
        > O(m * n) * O(2) ~= O(m * n) 

    Memory: 41.81 (Beats 55.93%)
    Space Complexity: O(m * n)
        > row의 길이가 n이가 col의 길이가 m인 2차원 배열 dp 사용에 O(m * n)
    """
    def solve_dp(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for idx1 in range(len(text1)):
            for idx2 in range(len(text2)):
                if text1[idx1] == text2[idx2]:
                    dp[idx1 + 1][idx2 + 1] = dp[idx1][idx2] + 1
                else:
                    dp[idx1 + 1][idx2 + 1] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])

        return dp[-1][-1]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        text1 = "abcde"
        text2 = "ace"
        output = 3
        self.assertEqual(
            Solution().longestCommonSubsequence(text1, text2),
            output
        )


if __name__ == '__main__':
    main()
