// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         int ans = 0;
//         for(int i = 0; i < prices.size(); i++)
//             for(int j = i + 1; j < prices.size(); j++)
//                 ans = max(prices[j] - prices[i], ans);

//         return ans;
//     }
// };

// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         int now = 1, l_idx = 0, r_idx = 0, ans = 0;
        
//         while(now < prices.size()) {
//             if(prices[now] < prices[l_idx]) {
//                 ans = max(ans, prices[r_idx] - prices[l_idx]);
//                 l_idx = now;
//                 r_idx = now;
//                 continue;
//             }
//             if(prices[now] > prices[r_idx])
//                 r_idx = now;
//             now++;
//         }
//         ans = max(ans, prices[r_idx] - prices[l_idx]);
//         return ans;
//     }
// };

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int ans = 0;
        for(int i = 1; i < prices.size(); i++) {
            ans = max(ans, prices[i] - buy);
            buy = min(buy, prices[i]);
        }
        
        return ans;
    }
};

