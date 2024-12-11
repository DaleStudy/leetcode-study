"""
풀이:
    1) lower case로 변형합니다.
    2) alpha numeric 인 문자만 string 배열에 담아줍니다.
    3) string 배열과 string 배열의 역순 배열을 비교해서 return 합니다.

시간 복잡도:
    1) s.lower() -> O(n) - 각 요소를 순회하며 lower case로 바꿔줍니다.
    2) for char in s: -> O(n) - 각 요소를 순회하면 isalnum() 여부를 확인합니다.
    3) string.append(char) -> O(1)
    4) string[::-1] -> O(n) - 각 요소를 순회합니다.

    결론: O(4n) 이므로 O(n) 입니다.

공간 복잡도: 
    1) string 배열 - O(n)
    2) string[::-1] - O(n)

    결론: O(n) 입니다.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        s = s.lower()
        for char in s:
            if char.isalnum():
                string.append(char)

        return string == string[::-1]
