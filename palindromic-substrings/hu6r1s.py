class Solution:
  """
  
  """
    def countSubstrings(self, s: str) -> int:
        cnt = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub and sub == sub[::-1]:
                    cnt.append(sub)
        return len(cnt)
