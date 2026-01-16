class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = (int)nums.size();
        int curMax = nums[0];
        int curMin = nums[0];
        int ans = nums[0];

        for (int i = 1; i < n; i++) {
            int x = nums[i];

            if (x < 0) swap(curMax, curMin);

            curMax = max(x, curMax * x);
            curMin = min(x, curMin * x);

            ans = max(ans, curMax);
        }
        return ans;
    }
};
