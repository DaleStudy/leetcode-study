class Solution:
  """
  브루트포스로 모두 탐색하면서 집어넣는 방법
  O(n^2)
  """
  def countSubstrings(self, s: str) -> int:
      cnt = []
      for i in range(len(s)):
          for j in range(i, len(s)):
              sub = s[i:j+1]
              if sub and sub == sub[::-1]:
                  cnt.append(sub)
      return len(cnt)
