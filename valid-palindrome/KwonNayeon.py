"""
Conditions:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

<Solution 1>
Time Complexity: O(n)
- 

Space Complexity: O(n)
- 

풀이 방법: 
- 
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        return False
"""
<Solution 2>
Time Complexity: O(n) 
- 팰린드롬일 경우, 각 문자를 한 번씩 검사함

Space Complexity: O(1)
- left, right 포인터 외에 추가 공간 사용 없음

풀이 방법: 
- 
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
