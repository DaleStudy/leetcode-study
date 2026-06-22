# import re
# # two pointers 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # remove all alphanumeric characters and convert all uppercase letters into lowercase letters
#         cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#         n = len(cleaned_s)
#         left, right = 0, n -1
#         while left < right: 
#             if cleaned_s[left] == cleaned_s[right]:
#                 left += 1 
#                 right -= 1
#             else:
#                 return False 
        
#         return True
# 7기 
# use two pointers 
# Time Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(cleaned_s) -  1
        while l < r :
            if cleaned_s[l] != cleaned_s[r]:
                return False 
            l += 1
            r -= 1
        return True 
