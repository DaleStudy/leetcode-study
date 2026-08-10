"""
시간복잡도 : O(T1 * T2)
공간복잡도 : O(T1) # T1에 짧은 문자열을 설정했기에 공간복잡도는 T1이 된다.

1. text1과 text2 중 더 짧은 쪽을 text1으로 설정한다.
2. T1과 T2를 각각 text1과 text2의 길이로 설정한다.
3. dp 배열을 T1 + 1 크기로 0으로 초기화한다.
4. text2의 각 문자(i)를 순회하면서 비교한다.
5. new_dp 배열을 T1 + 1 크기로 0으로 초기화한다.
6. text1의 각 문자(j)에 대해 순회하면서 비교한다.
7. text2[i - 1]과 text1[j - 1]가 같으면, new_dp[j]를 dp[j - 1] + 1로 설정한다.
8. 다르면, new_dp[j]를 max(new_dp[j - 1], dp[j])로 설정한다.
9. dp를 new_dp로 갱신하고, 마지막 원소를 반환한다.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text1, text2

        T1, T2 = len(text1), len(text2)
        dp = [0] * (T1 + 1)

        for i in range(1, T2 + 1):
            new_dp = [0] * (T1 + 1)

            for j in range(1, T1 + 1):
                if text2[i - 1] == text1[j - 1]:
                    new_dp[j] = dp[j - 1] + 1
                else:
                    new_dp[j] = max(new_dp[j - 1], dp[j])

            dp = new_dp

        return dp[-1]
