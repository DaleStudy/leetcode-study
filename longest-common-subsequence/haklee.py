"""TC: O(m * n), SC: O(m * n)

주어진 문자열의 길이를 각각 m, n이라고 하자.

아이디어:
- 두 문자열이 주어졌는데 끝이 같은 문자라고 하자. 이 경우 lcs의 길이는 각각의 문자열에서
  끝 문자를 제거한 문자열로 lcs의 길이를 구한 값에 1을 더한 값이다.
    - e.g.) abcz, bcdefz의 lcs 길이를 `x`라고 한다면,
            abc/z, bcdef/z에서 끝의 z가 같은 문자니까 이게 lcs에 들어간다 칠 수 있으므로,
            abc, bcdef의 lcs 길이는 `x - 1`이 된다.
- 두 문자열의 끝 문자가 다를 경우, 첫 번째 문자열의 끝 문자를 제거하고 구한 lcs의 길이나
  두 번째 문자열의 끝 문자를 제고하고 구한 lcs의 길이 둘 중 큰 값이 원래 문자열로 구한 lcs
  의 길이다.
    - e.g.) abcz, bcdefy의 lcs 길이를 `x`라고 한다면,
            abc, bcdefy의 lcs 길이와
            abcz, bcdef의 lcs 길이
            둘 중 더 큰 값을 취하면 된다.
- LCS는 유명한 알고리즘이므로 위의 설명을 시각적으로 잘 표현한 예시들을 온라인상에서 쉽게
  찾을 수 있다.
- 위의 아이디어를 점화식으로 바꾸면
    - 첫 번째 문자열의 앞 i글자로 만든 문자열과 두 번째 문자열의 앞 j글자로 만든 문자열의
      lcs의 길이를 lcs(i, j)라고 하자.
    - 첫 번째 문자열의 i번째 글자와 두 번째 문자열의 j번째 글자가 같은 경우 다음의 식이 성립.
        - lcs(i, j) = lcs(i-1, j-1) + 1
    - 다를 경우, 다음의 식이 성립.
        - lcs(i, j) = max(lcs(i-1, j), lcs(i, j-1))
- 위의 아이디어를 memoize를 하는 dp를 통해 구현할 수 있다. 자세한 내용은 코드 참조.

SC:
- 첫 번째 문자열의 앞 i글자로 만든 문자열과 두 번째 문자열의 앞 j글자로 만든 문자열의 lcs의
  길이를 관리.
- 그런데 아이디어에 제시된 점화식을 보면 i, j값에 대한 전체 배열을 저장할 필요 없이 i=k일때
  값을 구하려 한다면 i=k-1일때 구한 lcs값만 알고 있으면 충분하다.
- 즉, 배열은 현재 구하고자 하는 i값에 대한 j개의 아이템과 직전에 구한 j개의 아이템만 저장하면
  충분하다. 즉, text2의 길이인 O(n)이라고 볼 수 있다.
- 그런데 만약 text2의 길이가 text1보다 길면 이 둘을 바꿔치기해서 위의 공간복잡도를 O(m)이라고
  봐도 아이디어 자체는 똑같이 작동하지 않는가?
- 즉, O(min(m, n))

TC:
- dp 배열을 채우는 데에 마지막 문자가 같을 경우 단순 덧셈, 다를 경우 두 값 비교. 둘 다 O(1).
- 배열 채우는 것을 m * n회 반복하므로 총 O(m * n).
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            # 이 최적화까지 해주면 사용하는 메모리 크기가 많이 줄어들 수 있다.
            text1, text2 = text2, text1

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(2)]

        for i in range(1, len(text1) + 1):
            i_prev = (i + 1) % 2
            i_cur = i % 2
            for j in range(1, len(text2) + 1):
                dp[i_cur][j] = (
                    dp[i_prev][j - 1] + 1
                    if text1[i - 1] == text2[j - 1]
                    else max(dp[i_prev][j], dp[i_cur][j - 1])
                )

        return dp[i_cur][-1]
