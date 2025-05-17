/*
    풀이 :
        bottom-up dp 활용, 낮은 수부터 amount까지 차례로 해당 금액을 만들 수 있는 최소 동전 개수를 업데이트.
        amount가 0이면 동전 개수 0이므로 dp[0] = 0으로 초기화
        그 외의 초기값은 amount + 1로 설정
            (1짜리 동전으로 채우면 dp[amount] 최댓값 == amount이므로 amount + 1 그대로이면 채울 수 없는 케이스)

    coin 종류 : C, amount 크기 : A

    TC : O(A * C)
        amount의 크기 * coin 종류만큼 반복문

    SC : O(A)
        dp배열의 크기는 amount 크기에 비례
*/

class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            vector<int> dp(amount + 1, amount + 1);
    
            dp[0] = 0;
            for (int i = 0; i <= amount; i++)
            {
                for (auto coin : coins)
                {
                    if (i - coin >= 0)
                        dp[i] = min(dp[i - coin] + 1, dp[i]);
                }
            }
            if (dp[amount] == amount + 1)
                return -1;
            else
                return dp[amount];
        }
    };
