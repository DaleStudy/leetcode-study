"""
    TC: O(n)
    SC: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0
        for i in range(len(s)):
            if s[i] not in str_list:
                str_list.append(s[i])
            else:
                if max_length < len(str_list):
                    max_length = len(str_list)
                str_list = str_list[str_list.index(s[i])+1:]
                str_list.append(s[i])

        if max_length < len(str_list):
            max_length = len(str_list)

        return max_length

