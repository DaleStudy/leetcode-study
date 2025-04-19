"""
[문제풀이]
# Inputs
- string s
# Outputs
- palindrome 인지에 대한 true, false 여부
# Constraints
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
# Ideas
문자열 최대 길이 10^5 -> 2중 for문 불가능

우선 s를 순회하며,
- isalpha인 요소라면 lower 화 시켜서 새로운 문자열 p 에 붙이기
- 그리고 그 p가 p == p[::-1] 이면 true, 아니면 false

TC: O(n), SC: O(n)

[회고]
문제 조건에 all non-alphanumeric characters를 제외한 문자열을 기준으로
-> 즉, numeric도 고려해야한다!

너무 쉬운 해결방법인 [::-1]를 쓴 것 같아서,
해설 참고
-> 투 포인터

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""

        for c in s:
            if c.isalpha():
                t += c.lower()
            elif c.isalnum():
                t += c

        return t == t[::-1]

# 해설: 투 포인터 풀이
class Solution:
    def isPalindrome(s):
        low, high = 0, len(s) - 1
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            low, high = low + 1, high - 1
        return True

    isPalindrome("A man, a plan, a canal: Panama")


