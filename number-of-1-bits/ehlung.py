"""
n = 입력 정수 (이진수로 바꾸면 자릿수는 약 log n개)
시간 복잡도: O(log n) - bin 변환 O(log n) + 슬라이스·list 변환 O(log n) + 자릿수만큼 도는 반복문 O(log n)
공간 복잡도: O(log n) - bin이 만든 문자열과 binary_list에 자릿수(약 log n)만큼 들어감
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_list = list(bin(n)[2:])
        cnt = 0
        for n in binary_list:
            if n == "1":
                cnt += 1
        return cnt
