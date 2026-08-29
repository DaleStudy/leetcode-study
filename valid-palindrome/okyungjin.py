# [문제]
# https://leetcode.com/problems/valid-palindrome/description/

# [요구사항]
# 주어진 문자열이 팰린드롬인지 판별하는 함수를 작성한다.
# 팰린드롬이란?
# 1. 대문자가 있다면 소문자로 변환한다
# 2. 알파벳 or 숫자가 아니라면 제거한다.
# 3. 앞뒤로 읽었을 때 동일한 문자여야 한다.

# [접근법]
# - 문자열 전체를 공백 제거 & 소문자로 변환하지 않고, 투 포인터를 통해 lazy하게 연산한다.
# - 문자열 양 끝에 포인터를 선언하고, alphanumeric인 경우 소문자로 변환 후 두 문자를 비교한다. 다르면 False 리턴
# - alphanumeric이 아니면 alphanumeric 문자가 나올 때까지 이동한다.

# [복잡도]
# 시간 복잡도: O(N)
# 공간 복잡도: O(1)
class SolutionA:
    def isPalindrome(self, s: str) -> bool:

        # 문자열 양 끝 포인터 선언
        left = 0
        right = len(s) - 1

        while left < right:
            # alphanumeric 이 나올 때까지 왼쪽 포인터를 우측으로 이동
            while left < right and not isAlphaNumeric(s[left]):
                left += 1

            # alphanumeric 이 나올 때까지 오른쪽 포인터를 좌측으로 이동
            while left < right and not isAlphaNumeric(s[right]):
                right -= 1
            
            # 소문자로 변환해서 비교
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# 문자가 alphanumeric인지 판별하는 함수
# A ~ Z 혹은 a ~ z 혹은 0 ~ 9 이면 True를 반환
def isAlphaNumeric(ch: str) -> bool:
    return (
        ord('A') <= ord(ch) <= ord('Z')
        or ord('a') <= ord(ch) <= ord('z')
        or ord('0') <= ord(ch) <= ord('9')
    )


# SolutuionB: SoulutionA와 같은 로직인데 `isalnum` 내장함수 사용
# isAlphaNumeric 함수를 직접 구현하고 찾아보니 파이썬 내장함수가 있었다.

# [복잡도]
# 시간 복잡도: O(N)
# 공간 복잡도: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자열 양 끝 포인터 선언
        left = 0
        right = len(s) - 1

        while left < right:
            # alphanumeric 이 나올 때까지 왼쪽 포인터를 우측으로 이동
            while left < right and not s[left].isalnum():
                left += 1

            # alphanumeric 이 나올 때까지 오른쪽 포인터를 좌측으로 이동
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 소문자로 변환해서 비교
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
