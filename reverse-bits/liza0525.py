# 7기 풀이
# 시간 복잡도: O(1)
# - 해당 문제는 조건 자체가 32자릿수로 되어 있어 최대 32번까지만 계산
# 공간 복잡도: O(1)
# - result, idx와 같은 변수만 사용
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        idx = 0  # 자릿수 계산을 위한 앵커

        while n > 0:  # n이 0이 되기 전까지 돌린다.
            remainder = n % 2  # 수를 2로 나눴을 때의 나머지가 해당 자리수에서의 2진수 값 (0 or 1)
            quotient = n // 2  # 몫은 다음 루프의 피젯수로

            if remainder:
                # 나머지가 있는 경우에는 해당 2진수 자리수에 값이 있다.
                # reversed한 값을 계산해야 하기 때문에 32 - idx - 1의 자릿수로 변환
                # (문제 조건 상 32자릿수가 기준)
                # 변환한 후 result에 값을 더해준다.
                result += 2 ** (32 - idx - 1)

            n = quotient
            idx += 1  # 자릿수를 하나 올린다

        return result
