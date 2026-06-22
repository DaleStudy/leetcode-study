# 시간 복잡도: O(log n)
# - 2로 계속 나누고, 이는 2진수 자릿수 만큼 반복하기 때문
# 공간 복잡도: O(1)
# - 변수 몇 개만 사용

class Solution:
    # 어떤 수를 2진수로 변환하는 과정은 2로 나눈 후, 그 나머지(1 또는 0)을 가장 높은 자리 수부터 순차로 나열하고
    # 몫을 그 다음 회차의 피제수로 사용하면 된다.
    # 해당 문제는 나열하지 않고 대상 수를 2로 나눌 때 매 회차의 나머지를 더해줌으로써 풀 수 있다.
    def hammingWeight(self, n: int) -> int:
        bits_sum = 0
        while n >= 1:
            # 모듈로 연산으로 나머지 계산한다.
            remainder = n % 2

            # 나머지 값을 결과 값에 더한다.
            bits_sum += remainder

            # 몫은 다음 회차 피제수로 사용한다.
            n = n // 2
        
        return bits_sum


# 7기 풀이
# 시간 복잡도: O(log n)
# - 2로 계속 나누고, 이는 2진수 자릿수 만큼 반복
# 공간 복잡도: O(1)
# - 고정된 변수(quotient, remainder)만 사용
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 10진수를 2진수로 변환하는 과정은 2로 계속 나누면서 그 나머지 값들을 순차적으로 나열하는 것이다.
        # 이 때 문자열로 만들지 않고 바로 result에 더해가면 답이 될 수 있음
        result = 0

        while n > 0:
            # 몫과 나머지 계산
            quotient, remainder = n // 2, n % 2

            # 나머지는 result에 더함
            result += remainder

            # 몫은 다음 피제수로 사용
            n = quotient

        return result
