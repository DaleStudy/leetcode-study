# https://leetcode.com/problems/valid-palindrome

# re.sub -> O(n)
# lower() -> O(n)
# reverse -> O(n)
# 최종 시간 복잡도 : O(n) + O(n) + O(n) + O(n) = O(n)

# s_pali -> 최대 O(n)
# s_pali_reverse -> O(n)
# 최종 공간 복잡도 : O(n)

import re

class Solution(object):
    def isPalindrome(self, s):
        s_pali = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s_pali_reverse = s_pali[::-1]

        if s_pali == s_pali_reverse:
            return True
        else:
            return False
