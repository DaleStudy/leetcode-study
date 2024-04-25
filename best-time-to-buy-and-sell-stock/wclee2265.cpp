// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Time Complexity : O(n)
// Space Complexity : O(1)

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int minimum = prices[0];
        int ans = 0;
        for(int i=1; i<n; i++) {
            ans = max(ans, prices[i] - minimum);
            minimum = min(minimum, prices[i]);
        }
        return ans;
    }
};
