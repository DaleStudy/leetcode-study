# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

"""
문제:
    - 정수 n이 주어질 때, 0부터 n까지 각 i에 대해 i의 이진 표현에 포함된 1의 개수를 구한다
    - 결과는 길이 n + 1인 배열 ans로 반환한다 (ans[i] = i의 1의 개수)
    - 0 <= n <= 10^5

복잡도:
    n: 입력 정수 n
    Time: O(n)
    Space: O(1)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        offset = 1

        for num in range(1, n + 1):
            if num == offset * 2:
                offset = num
            dp.append(dp[num - offset] + 1)

        return dp
