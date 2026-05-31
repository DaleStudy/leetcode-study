// class Solution {
// public:
//     int lengthOfLIS(vector<int>& nums) {
//         int n = nums.size(), maxi, ans = 1;
//         vector<int> dp(n, 0);
        
//         dp[0] = 1;
//         for(int i = 1; i < n; i++) {
//             maxi = 0;
//             for(int j = 0; j < i; j++)
//                 if(nums[j] < nums[i] && maxi < dp[j])
//                     maxi = dp[j];
//             dp[i] = maxi + 1;
//             ans = max(dp[i] , ans);
//         }

//         return ans;
//     }
// };

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> sub;

        for(int num : nums) {
            auto it = lower_bound(sub.begin(), sub.end(), num);
            int idx = it - sub.begin();
            if(idx == sub.size())
                sub.push_back(num);
            else
                sub[idx] = num;
        }

        return sub.size();
    }
};

