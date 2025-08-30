"""
# Intuition
소문자 변환, 영숫자 제외한 문자 제거
reverse와 비교

# Approach
1. non-alphanumeric(isalpha/isnum or 정규식) 일 때
2. lower()
3. 위 객체를 비교

- chars = "" 와 같이
빈 문자열을 만들고 반복문을 돌며 chars += char 형태로 문자를 하나씩 추가하면, 매번 새로운 문자열 객체를 생성하기 때문에 성능 비용이 큼.
  -> 리스트에 하나씩 추가한 뒤, 마지막에 "".join() 메서드 사용

# Complexity
- Time complexity : O(N)
- Space complexity : O(N)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        result = "".join(chars)

        # list comprehension
        # chars = "".join([char.lower() for char in s if char.isalnum()])

        return result == result[::-1]


sol = Solution()
s = "A man, a plan, a canal: Panama"

print(sol.isPalindrome(s))


# Pointer : O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            # while left < right and not s[left].isalnum():
            #     left += 1
            # while left < right and not s[right].isalnum():
            #     left -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


""" 전처리 필요함
class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        for i in range(len(chars)//2):
            left = chars[i]
            right = chars[len(chars) - 1 - i]

            if left != right:
                return False
        
        return True
"""

""" 정규식
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return chars == chars[::-1]
"""

"""
# non-alphanumeric
- isalpha() 
  - 문자열이 모두 알파벳(영문)으로만 구성되어 있는지 확인
  - 한글, 일본어 등 다른 언어의 문자도 포함 ('안녕하세요'.isalpha() → True)
  - 공백, 숫자, 특수문자 포함 X
- isnumeric()
  - 문자열이 모두 숫자로만 구성되어 있는지 확인
  - 숫자는 단순히 아라비아 숫자(0-9)뿐만 아니라, 유니코드 숫자(예: ①, ², 한자 숫자)도 포함 ('①②③'.isnumeric() → True)
  - 소수점(.)이나 음수 부호(-)는 숫자로 간주하지 X
- isalnum()
  - isalpha()와 isnumeric()의 조건을 합친 것으로, 문자열이 모두 알파벳 또는 숫자로 구성되어 있는지 확인

# 객체 역순
- .reverse()
  - list 객체에만 사용
  - 원본 수정, 반환값 None
- reversed()
  - 리스트, 튜플, 문자열 등 모든 iterable 객체에 사용 가능
  - 새로운 역순 'iterator' 객체를 반환, 원본 객체 변경 X 
  - 반환된 이터레이터는 리스트나 튜플 등으로 변환하여 사용해야 함. 메모리 효율이 중요한 경우 유용
- 슬라이싱 [::-1]
  - 리스트, 튜플, 문자열 등 모든 iterable 객체에 사용 가능
  - 원본을 복사하여 역순으로 정렬된 새로운 객체를 반환, 원본 객체 변경 X 
  - 원본 전체를 복사하므로 메모리 사용량이 reversed() 보다 더 많을 수 있다

* iterator
데이터의 순차적인 접근 방식을 정의하는 객체일 뿐, 그 자체로 모든 데이터를 메모리에 담고 있는 리스트나 튜플과 같은 직접적인 데이터 구조가 아니다.
"""
