"""
[Problem]
https://leetcode.com/problems/valid-palindrome/description/

모든 대문자를 소문자로 변환하고 알파벳과 숫자가 아닌 문자들을 전부 제거한 이후에 앞에서 부터 읽으나 뒤에서 부터 읽으나 동일하게 읽힌다면, 그 문장은 회문입니다.
영숫자 문자들은 알파벳과 숫자들을 포함합니다.

[Brainstorming]
leftPosition과 rightPosition을 두고, 비교하면서 아닐 경우 false를 return한다. => O(s.length)

[Complexity]
N: s.length
Time: O(1/2 * N) => O(N)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s:str)-> bool:
        leftPos, rightPos = 0, len(s) - 1
        while leftPos < rightPos:
            while not s[leftPos].isalnum() and leftPos < rightPos:
                leftPos += 1
            while not s[rightPos].isalnum() and leftPos < rightPos:
                rightPos -= 1

            if s[leftPos].upper() != s[rightPos].upper():
                return False
            leftPos += 1
            rightPos -= 1
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama") == True)
print(sol.isPalindrome("race a car") == False)
print(sol.isPalindrome(" ") == True)
print(sol.isPalindrome("0P") == False)
print(sol.isPalindrome("a") == True)
