class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0;
        int ans = -1e5;
        for (int n : nums)
        {
            // 이전까지 합이 음수라면 무조건 다시 시작하는게 이득
            if (cur < 0)
            {
                cur = 0;
            }
        
            cur += n;
            ans = max(cur, ans);
        }

        return ans;
    }
};
