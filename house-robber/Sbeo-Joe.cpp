class Solution {
public:
    int map[101];
    int rob(vector<int>& nums) {
        
        memset(map, -1, sizeof(map));
        int ret = -1;
        for(int i = 0; i < nums.size(); i++){
            ret = max(ret, solve(nums, i));
        }
        return ret;
    }

    int solve(vector<int>& nums, int here) {
        if(here >= nums.size()) return 0;
        
        int& ret = map[here];
        if(ret != -1) return ret;
        ret = nums[here];
        for(int there = here + 2; there < nums.size(); there++){
            ret = max(ret, solve(nums, there) + nums[here]);
        }
        return ret;
    }

};
