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
