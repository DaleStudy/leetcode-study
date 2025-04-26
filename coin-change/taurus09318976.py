'''
이 문제는 동적 프로그래밍을 이용한 방식이
1) 모든 가능한 경우를 체계적으로 계산할 수 있고,
2) 중복 계산을 피할 수 있고,
3) 최적의 값을 보장한다는 점에서 좋은 풀이방식임.
다만, 
1) amount가 클 경우 메모리 사용이 많을 수 있고,
2) 동전의 가치가 매우 작을 경우 시간이 오래 걸릴 수 있다는 점에서 단점이 있음
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 초기화
        # dp 배열: 각 금액을 만들기 위한 최소 동전 수를 저장
        # amount + 1로 초기화 (불가능한 경우를 구분하기 위해)
        # 0원을 만들기 위한 동전 수는 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # 동적 프로그래밍 실행:
        # 1원부터 amount원까지 순차적으로 계산
        for i in range(1, amount + 1):
            # 각 동전에 대해 시도
            for coin in coins:
                # 현재 금액이 동전보다 크거나 같은 경우에만 시도
                if i >= coin:
                    # 현재 동전을 사용하는 경우와 사용하지 않는 경우 중 최소값 선택
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 결과 반환
        # amount원을 만들 수 없는 경우 -1 반환
        return dp[amount] if dp[amount] != amount + 1 else -1

        # 시간 복잡도 (Time Complexity): O(n * m)
            #n: amount
            #m: coins의 길이
            #이유:
                #amount까지의 모든 금액에 대해 계산
                #각 금액마다 모든 동전을 확인
                #따라서 시간 복잡도는 O(n * m)
        # 공간 복잡도 (Space Complexity): O(n)
            # n: amount
            #이유:
                # dp 배열의 크기가 amount + 1
                # 추가적인 메모리 사용 없음
                # 따라서 공간 복잡도는 O(n) 