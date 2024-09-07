class Solution {
    // Time complexity: O(n)
    // Space complexity: O(1)
public:
    int maxProduct(vector<int>& nums) {

        int result = nums[0];
        int previous_max = 1;
        int previous_min = 1;

        for (int num : nums) {
            int temp = previous_max;
            previous_max = max({num, previous_max * num, previous_min * num});
            previous_min = min({num, temp * num, previous_min * num});
            result = max(result, previous_max);
        }

        return result;
    }
};
