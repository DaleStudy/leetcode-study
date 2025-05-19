class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int min = INT_MAX;
            int profit = 0;
    
            for(int i = 0; i < prices.size(); i++){
                if(prices[i] < min)
                    min = prices[i];
                
                profit = max(profit, prices[i] - min);
            }
    
            return profit;
        }
    };
