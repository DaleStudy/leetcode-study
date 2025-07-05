class Solution {
public:
    int robsearch(vector<int>& nums, int start, int end) {
        int prev = 0;
        int prevprev = 0;

        for(int i = start; i <= end; i++){
            int curr = max(prev, nums[i] + prevprev);

            prevprev = prev;
            prev = curr;
        }

        return prev;
    }

    int rob(vector<int>& nums) {
        int len = nums.size();

        if(len == 0) 
            return 0;
        if(len == 1)
            return nums[0];

        return max(robsearch(nums, 0, len - 2), robsearch(nums, 1, len - 1));
    }
};
