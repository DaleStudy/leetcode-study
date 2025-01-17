"""
직접 풀지 못해 알고달레 풀이를 참고했습니다. https://www.algodale.com/problems/coin-change/

Solution:
    1) BFS를 통해 모든 동전을 한번씩 넣어보며 amount와 같아지면 return

(c: coins의 종류 갯수, a: amount)
Time: O(ca)
Space: O(a)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(0, 0)])  # (동전 갯수, 누적 금액)
        visited = set()

        while q:
            count, total = q.popleft()
            if total == amount:
                return count
            if total in visited:
                continue
            visited.add(total)
            for coin in coins:
                if total + coin <= amount:
                    q.append((count + 1, total + coin))
        return -1
