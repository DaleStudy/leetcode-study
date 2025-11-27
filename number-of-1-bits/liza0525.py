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
