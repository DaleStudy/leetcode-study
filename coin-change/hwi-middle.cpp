class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount < 1)
        {
            return 0;
        }

        vector<int> v(amount);
        return solve(coins, amount, v);
    }

    int solve(vector<int>& coins, int amount, vector<int>& count)
    {
        if (amount < 0) return -1;
        if (amount == 0) return 0;
        if (count[amount - 1] != 0) return count[amount - 1];

        int min = INT_MAX;
        for (int coin : coins) 
        {
            int res = solve(coins, amount - coin, count); // coin을 사용
            if (res >= 0 && res < min) // 결과가 유효하고 현재 최솟값보다 작으면 업데이트
            {
                min = res + 1; // coin을 미리 사용하고 찾은 값이므로 1 더함
            }
        }

        count[amount - 1] = (min == INT_MAX) ? -1 : min;
        return count[amount - 1];
  }
};
