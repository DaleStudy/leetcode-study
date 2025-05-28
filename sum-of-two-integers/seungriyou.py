# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        [Complexity]
            - TC: O(1)
            - SC: O(1)

        [Approach]
            덧셈 구현 시 주요한 요소는 carry와 value 값이다.
            예를 들어 이진수 11과 101의 덧셈을 생각해보면, 각 자리에서 발생하는 carry와 value는 다음과 같다.
                       a =  0   1   1
                       b =  1   0   1
                       ---------------
                value)      1   1   0   (= a ^ b)
                carry)      0   0   1   (= a & b)
            이때, 어떤 자리에서 발생한 carry는 한 칸 left shift 되어 다시 덧셈을 수행하듯 적용되어야 함에 주의한다.
                value)      1   1   0
                carry)  0   0   1   0   (<<= 1)

            이 과정을 carry가 0이 될 때까지 반복해나간다.
                value)  0   1   0   0   (= a ^ b)
                carry)  0   1   0   0   (= (a & b) << 1)

                value)  0   0   0   0   (= a ^ b)
                carry)  1   0   0   0   (= (a & b) << 1)

                value)  1   0   0   0   (= a ^ b)               -> RESULT
                carry)  0   0   0   0   (= (a & b) << 1)        -> END

            하지만 파이썬에서는 int를 32bit 보다 큰 메모리에 저장하므로 음수가 들어올 경우에 대비해 다음의 작업을 추가로 수행해야 한다.
                - 음수가 들어온다면 carry가 32bit를 넘어서도 계속 더해질 것이므로, while 문 조건식에의 carry에 32bit masking을 수행한다.
                - (b & mask) == 0이지만 b > 0인 경우에는 a의 32bit 범위 밖에 overflow가 존재하는 것이므로, 결과 값에도 32bit masking을 수행한다.
        """

        mask = 0xffffffff   # 32bit masking

        # carry가 0이 될 떄까지 반복 (음수가 들어오는 경우, 32bit masking 후 확인)
        while (b & mask) != 0:
            a, b = a ^ b, (a & b) << 1      # value, carry

        return (a & mask) if b > 0 else a   # 음수 (overflow) 처리
