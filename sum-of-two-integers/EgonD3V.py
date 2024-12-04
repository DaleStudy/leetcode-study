from unittest import TestCase, main


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.solve_bit(a, b)

    """
    Runtime: 26 ms (Beats 94.94%)
    Time Complexity: O(log max(a, b)) ~= O(1)
        - a와 b를 and 연산 후 왼쪽으로 shift한 값을 b에 할당하는데 모두 비트연산이므로 O(1)
        - b의 값이 왼쪽 shift에 의해 감소하므로 log(b)
            - 단 b의 값은 a & b에 의해 결정되므로 log max(a, b)
        - 전제 조건에서 a, b는 모두 절대값 1000 이하의 값이므로, 최대 10회의 shift 연산만 발생하므로, O(10) ~= O(1)
        > O(log max(a, b)) < O(10) ~= O(1)
        
    Memory: 16.52 (Beats 18.98%)
    Space Complexity: O(1)
        > input에 무관하게 정수형 변수들만 사용하므로 O(1)
    """
    def solve_bit(self, a: int, b: int) -> int:
        COMPLEMENT_MASK = 0xFFF

        while b != 0:
            carry = a & b
            a = (a ^ b) & COMPLEMENT_MASK
            b = (carry << 1) & COMPLEMENT_MASK

        return a if a <= 0x7FF else ~(a ^ COMPLEMENT_MASK)


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        a = -1
        b = 1
        output = 0
        self.assertEqual(Solution().getSum(a, b), output)


if __name__ == '__main__':
    main()
