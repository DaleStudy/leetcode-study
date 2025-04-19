"""
[문제풀이]
# Inputs
- 양인 정수 n
# Outputs
- number of set bits => 이진수 값의 1 개수
# Constraints
- 1 <= n <= 2^31 - 1
# Ideas
1. 반복문
2로 나눠서 몫 나머지 -> 나머지가 1인지 0인지 체크
그 몫을 또 2로 나눠서 몫, 나머지 ->


11
2-> 5, 1
2-> 2, 1
2-> 1, 0
2-> 0, 1

몫이 0이 될 때 까지 반복

TC: log2N? SC: 1

[회고]
시간 복잡도가 log2N인가?
-> O

해설은 어떤지 궁금
->

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n > 0:
            n, bit = n // 2, n % 2
            if bit == 1:
                ret += 1

        return ret

# 해설

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt

