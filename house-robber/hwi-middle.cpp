class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size() + 1;
        vector<int> d(len);
        d[0] = 0;
        d[1] = nums[0];
        for(int i = 2; i < len; ++i)
        {
            d[i] = max(d[i - 1], d[i - 2] + nums[i - 1]);
        }

        return d[len - 1];
    }
};
