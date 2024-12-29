# O((LogN)^N) times, O(1) spaces
class Solution:
    def countSubstrings(self, s: str) -> int:
        sub_str_len = 1
        result = 0

        while sub_str_len <= len(s):
            start_idx = 0
            while start_idx + sub_str_len <= len(s):
                sub_str = s[start_idx:start_idx+sub_str_len]
                if sub_str == sub_str[::-1]:
                    result += 1
                start_idx += 1

            sub_str_len += 1
        

        return result
