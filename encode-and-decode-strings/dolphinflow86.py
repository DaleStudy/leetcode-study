# 1) Prepend each word with its length and a delimiter '%'.
# TC: encode O(N) where N is the len(str), decode O(N) where N is the len(s)
# SC: O(N) for storing the encoded string
class Solution:

    def encode(self, strs: list[str]) -> str:
        answer = ""
        for s in strs:
            answer += f"{len(s)}%{s}"
        return answer

    def decode(self, s: str) -> list[str]:
        left = 0
        right = 0
        str_len = len(s)

        result = []
        while right < str_len:
            while s[right] != "%":
                right += 1

            num_len = int(s[left:right])
            start = right + 1
            word = s[start : start + num_len]
            result.append(word)

            left = start + num_len
            right = left

        return result
