#idea: -
#Time Complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        def check_func(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            odd = check_func(i, i)
            even = check_func(i, i+1)
            if len(odd) > len(even):
                longer = odd 
            else: 
                longer = even

            if len(longer) > len(ans):
                ans = longer

        return ans


