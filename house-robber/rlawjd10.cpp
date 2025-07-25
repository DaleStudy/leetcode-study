class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];

        int prev2 = 0;  // 두 칸 전 (현재 집 털기)
        int prev1 = 0;  // 한 칸 전 (현재 집 안털기)

        for (int num : nums) {
            int current = max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
};

