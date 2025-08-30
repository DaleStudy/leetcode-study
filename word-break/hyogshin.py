"""
풀이 방법
- for 루프로 주어진 문자열을 돌면서 wordDict에 있는 단어와 매칭되면 해당 인덱스 dp를 True로 변경
- True인 dp로부터 또 다른 단어가 사전에 매칭되면 다시 dp를 True로 변경
- 문자열 길이 인덱스의 dp[len(str)] 가 True인 경우 모든 단어가 사전에 있는 단어로 대체 가능하므로 True 반환

시간 복잡도: O(n^2)
- for loop * n + for loop * 최대 n -> O(n^2)
- s[j:i] 를 wordDict에서 찾는 행위 -> O(m)

공간 복잡도: O(n)
- dp 배열 크기 -> O(n)
- wordDict 크기 -> O(m)
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      dp = [False] * (len(s) + 1)
      dp[0] = True
      for i in range(1, len(s) + 1):
        for j in range(i):
          if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break
      return dp[len(s)]

