class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int prod_min = 1, prod_max = 1, ans = nums[0];

        for(int num : nums) {
            int tmp = prod_min;
            prod_min = min(prod_min * num, prod_max * num);
            prod_min = min(prod_min, num);
            prod_max = max(tmp * num, prod_max * num);
            prod_max = max(prod_max, num);
            ans = max(ans, prod_max);
        }

        return ans;
    }
};

