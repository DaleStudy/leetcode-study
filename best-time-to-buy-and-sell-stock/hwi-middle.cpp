class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int minPrice = prices[0];
        int len = prices.size();
        for (int i = 0; i < len; ++i)
        {
            res = max(res, prices[i] - minPrice);
            minPrice = min(minPrice, prices[i]);
        }

        return res;
    }
};
