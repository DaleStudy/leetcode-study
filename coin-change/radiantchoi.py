from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS를 이용한 최소 동전 개수 찾기
        # 동전을 하나씩 추가하면서 만들 수 있는 금액을 탐색 (레벨별 탐색)
        # BFS 특성상 먼저 도달하는 경로가 최소 동전 개수 보장
        # dp[i]: amount가 i일 때 최소 동전 사용 횟수
        # 모든 경우 방법이 없다고 가정하고 -1로 초기화
        dp = [-1 for _ in range(amount + 1)]
        
        # bfs 셋업 - 합이 0인 노드를 방문하고, 방문 처리
        dp[0] = 0
        # 큐의 각 요소: [사용한 동전 개수, 현재까지의 합]
        # 시작 상태: 동전 0개, 합 0
        q = deque([[0, 0]])

        while q:
            # current[0]: 사용한 동전 개수, current[1]: 현재까지의 합
            current = q.popleft()

            # 각각의 동전은 무한히 사용할 수 있으므로, 가능한 경우 모두 탐색
            for coin in coins:
                estimated = current[1] + coin

                # estimated <= amount: 목표 금액을 초과하지 않는 경우만 탐색
                # dp[estimated] == -1: 아직 방문하지 않은 금액 (BFS 특성상 최초 도달이 최적)
                # 두 조건 모두 통과하면 큐에 추가하여 계속 탐색
                if estimated <= amount and dp[estimated] == -1:
                    used = current[0] + 1
                    dp[estimated] = used

                    new = [used, estimated]
                    q.append(new)

        # dp[amount]가 -1이면 모든 경우 방법이 없다는 의미이므로 -1 반환
        # 그렇지 않다면 dp[amount] 반환
        return dp[amount]
