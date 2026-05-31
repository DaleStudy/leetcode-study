"""
# Intuition
이진수로 변환 후 1 세기

# Approach
n % 2 (나머지)가 1이면 cnt += 1

# Complexity
- Time complexity : O(logN)
  - 10진수 n을 2진수로 변환했을 때 비트의 개수는 log2(n)에 비례. 따라서 이 루프는 약 log2(n)번 반복
- Space complexity : O(N)
  - bin(n) 함수는 n의 2진수 표현을 담는 새로운 문자열을 생성. 이 문자열의 길이는 logn에 비례 : O(logN)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        while n > 0:
            cnt += n % 2
            n //= 2

            # if n % 2 == 1:
            #     cnt += 1
            # n = n // 2

        return cnt


"""    
class Solution:
    def hammingWeight(self, n: int) -> int:

        # return bin(n).count("1")

        cnt = 0

        for b in bin(n):
            if b == 1:
                cnt += 1

        return cnt
"""

sol = Solution()
print(sol.hammingWeight(11))


### 6기 ###
from collections import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:

        binary = []

        # 반복 - 시작/종료 조건
        while n != 0:
            # n/2의 몫과 나머지 둘 다 필요
            n, remainder = divmod(n, 2)
            binary.append(remainder)

        return Counter(binary)[1]


# 비트 시프트(Bit Shift) 연산
def hammingWeight_bit(n: int) -> int:
    count = 0

    while n != 0:
        count += n & 1  # 1. n의 가장 오른쪽 비트가 1이면 더함
        n >>= 1  # 2. n의 모든 비트를 오른쪽으로 한 칸 이동 (n을 2로 나눔)

    return count


""" Q. binary를 선언할 때 list / str 중 효율적인것은?
- list : O(1)
- str
  - Python에서 문자열은 불변(Immutable) 자료형
  - 문자열에 문자를 하나씩 추가할 때마다 새로운 문자열 전체가 생성되고 기존 문자열이 복사되어야 함 O(n^2)
"""
