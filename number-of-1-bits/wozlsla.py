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
