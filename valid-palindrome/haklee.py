"""TC: O(n), SC: O(n)

아이디어: 
문자열을 보고 숫자 혹은 알파벳인 문자만 뽑아서 새 문자열을 만들고, 대문자는 소문자로 바꾼다.
구현이 어렵지는 않지만 귀찮을 수 있는데, python에는 위 과정을 `isalnum()`, `lower()` 함수로
쉽게 처리할 수 있다. 마지막으로 새로 만든 문자열을 뒤집어서 원래 문자열과 같은지 확인하면 된다.


SC:
- 문자열을 필요한 문자만 남기는 과정에서 O(n).
- 문자열을 뒤집어서 저장. O(n).
- 즉, O(n).

TC:
- 문자열을 필요한 문자만 남기는 과정에서 O(n).
- 문자열 뒤집기. O(n).
- 새로 만든 문자열과 뒤집은 문자열 palindrome 체크. O(n).
- 즉, O(n).
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (l := [c.lower() for c in s if c.isalnum()]) == l[::-1]
