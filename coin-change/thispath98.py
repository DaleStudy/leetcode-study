class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Intuition:
            dp 배열에 이전 금액에 대한 최소 개수를 저장해두고
            갱신하는 방식으로 작동한다.

            for 루프를 돌면서 현재 가격에서 coin만큼의 가격을
            뺐을 때 거슬러줄 수 있다면, 그 값에서 1개를 더해준
            개수를 prev_coins에 저장한다.

            이후 prev_coins가 존재하면 현재 인덱스에서 거슬러줄 수 있는
            동전의 최소 개수를 갱신한다.

        Time Complexity:
            O(amount x coins.length):
                amount 만큼 루프를 순회하는데 각 루프마다
                coins.length 만큼 prev_coins 배열을 만든다.

        Space Complexity:
            O(amount):
                amount만큼의 크기를 가지는 dp 배열을 저장한다.
        """
        dp = [0 for _ in range(amount + 1)]

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            if dp[i]:
                continue

            prev_coins = [dp[i - coin] + 1 for coin in coins if i >= coin and dp[i - coin] > 0]
            if prev_coins:
                dp[i] = min(prev_coins)

        answer = -1 if amount > 0 and dp[amount] == 0 else dp[amount]
        return answer
