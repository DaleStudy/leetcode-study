"""
Conditions:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

<Solution 1>
Time Complexity: O(n)
- 문자열 길이(n)에 비례함
- 정규식 처리, 소문자 변환, 역순 비교 모두 O(n)

Space Complexity: O(n)
- 변환된 문자열과 역순 문자열을 저장하는 공간이 필요함

풀이 방법: 
- 문자열에서 알파벳과 숫자만 남기고 모두 소문자로 변환
- 변환된 문자열과 그 역순이 같은지 비교
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
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
- 양쪽 끝에서 시작하는 두 포인터(left, right)를 활용한 방법
- 알파벳/숫자가 아닌 문자는 건너뛰며 포인터 이동
- 두 포인터가 가리키는 문자가 다르면 즉시 False 반환
- 모든 비교가 일치하면 True 반환
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
