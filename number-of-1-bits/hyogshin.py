'''
풀이
- 파이썬3 내장 함수인 bit_count() 함수 이용

시간 복잡도: O(1)

공간 복잡도: O(1)
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
        
