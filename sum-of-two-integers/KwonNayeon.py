"""
Constraints:
- -1000 <= a, b <= 1000

Time Complexity: O(1)

Space Complexity: O(1)
- 추가 공간을 사용하지 않고 입력받은 변수만 사용

풀이방법:
1. XOR(^)연산을 통해 캐리를 제외한 각 자리의 합을 구함
2. AND(&)연산 후 왼쪽 시프트(<<)로 다음 자리로 올라갈 캐리를 구함
3. 캐리가 0이 될 때까지 1-2 과정을 반복
"""
# Solution 1: 이해하기 쉬운 버전
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            current_sum = a ^ b

            next_carry = (a & b) << 1

            a = current_sum
            b = next_carry

        return a

# Solution 2: 최적화 버전
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a, b = a ^ b, (a & b) << 1

        return a

