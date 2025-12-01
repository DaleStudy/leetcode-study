'''
Approach
- 파이썬에서 제공되는 메소드를 사용해서 문자열 필터링 처리후 왼쪽과 오른쪽 값을 비교

Time Complexity: O(N)
- 문자열 s의 길이를 N이라고 할 때, 문자열을 순회하며 필터링하는 데 O(N) 시간이 걸림
- 이후 필터링된 문자열을 뒤집어 right 값을 만드는 데도 O(N) 시간이 걸림
- left와 right 값을 비교하는 데도 O(N) 시간이 걸림

Space Complexity: O(N)
- 필터링된 문자열을 저장하는 데 O(N) 공간이 필요함
- left와 right 값을 저장하는 데도 각각 O(N) 공간이 필요함
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자열이 아닌 경우만 소문자 변환 필터링
        char_str = [char.lower() for char in s if char.isalnum()]
        # 왼쪽 값
        left = ''.join(char_str)
        # 오른쪽 값
        right = ''.join(char_str[::-1])

        return left == right
