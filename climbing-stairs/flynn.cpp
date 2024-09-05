class Solution {
public:
int climbStairs(int n) {
vector<int> memo(2, 1);

        for (int i = 2; i <= n; i++) {
            memo.push_back(memo[i - 1] + memo[i - 2]);
        }

        return memo[n];
    }

};
