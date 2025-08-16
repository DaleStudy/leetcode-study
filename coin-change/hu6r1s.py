from collections import deque

class Solution:
    """
    1. 가장 큰 수부터 차례대로 빼면서 확인 - 틀린 풀이
    가장 큰 수부터 차례대로 빼면 안되는 경우가 있음
    coins = [186,419,83,408], amount = 6249
    이건 419부터 안될때까지 빼는 방식으로 되지 않음, 즉 최적의 금액을 찾아야 함.
    그리디 같은 문제일 듯

    """
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        result = 0
        for coin in coins:
            while amount >= coin:
                amount -= coin
                result += 1
        
        if amount:
            return -1
        return result
    """
    """
    - BFS를 사용하여 "동전 합"을 0에서 시작해 amount까지 도달하는 최소 단계를 탐색
    - 큐의 원소: (cnt, total)
        cnt   : 현재까지 사용한 동전 개수
        total : 현재까지 만든 합
    - visited 집합으로 이미 방문한 합을 중복 탐색하지 않게 함
    - 첫 번째로 amount에 도달하는 순간이 최소 동전 개수 (BFS 특성상)
    
    시간 복잡도:
    - 최악의 경우 모든 합(0 ~ amount)을 탐색하며,
      각 합에서 최대 len(coins)개의 새로운 상태를 큐에 넣음
    - O(amount × n), n = len(coins)

    공간 복잡도:
    - visited 집합: 최대 amount+1 크기
    - 큐(queue): 최악의 경우 O(amount × n) 상태 저장 가능
    - O(amount)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        def bfs():
            queue = deque([(0, 0)])
            visited = set()
            while queue:
                cnt, total = queue.popleft()
                if amount == total:
                    return cnt
                if total in visited:
                    continue
                visited.add(total)

                for coin in coins:
                    if coin + total <= amount:
                        queue.append((cnt + 1, total + coin))
            return -1
        
        return bfs()
