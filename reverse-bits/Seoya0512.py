'''
파이썬 내장 함수 사용
- format 함수로 정수 n을 32비트 이진수로 변환한 뒤, 역수로 뒤집어 다시 정수로 변환 

Time Complexity: O(1)
Space Complexity: O(1)
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n,'032b')[::-1], 2)
