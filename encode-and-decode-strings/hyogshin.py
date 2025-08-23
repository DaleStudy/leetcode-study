"""
풀이 방법
- 암호화 시  (단어의 개수) + '#' + (단어) 형식 사용

시간 복잡도: O(n)
- encode: join 이 모든 문자열을 이어붙임 -> O(n)
- decode: while 문 -> O(n)

공간 복잡도: O(n)
- encode: 새로운 문자열 생성 -> O(n)
- decode: ans 리스트 -> O(n)
"""

from typing import List
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
      return ''.join(f'{len(s)}#{s}' for s in strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s):

      ans = []
      i = 0
      while i < len(s):
        j = i
        while s[j] != '#':
          j += 1
        length = int(s[i:j])
        start = j + 1
        end = start + length
        ans.append(s[start:end])
        
        i = end
      return ans

if __name__ == "__main__":
    sol = Solution()

    cases = [
        ["abc", "a#b", "", "hello"],
        ["", ""],                      # 빈 문자열 2개
        ["#", "##", "###"],            # 해시 포함
    ]
    for arr in cases:
        enc = sol.encode(arr)
        dec = sol.decode(enc)
        print(arr == dec, arr, "->", enc[:50] + ("..." if len(enc) > 50 else ""))


