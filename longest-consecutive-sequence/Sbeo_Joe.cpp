class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        set<int> us{nums.begin(), nums.end()};
        int ret = 1;
        vector<int> vec(us.begin(), us.end());
        int prevNum = vec[0];
        int ret_candi = 1;
        for(int i = 1; i < vec.size(); i++){
            if(vec[i] - vec[i-1] == 1){
                ret_candi++;
                ret = max(ret, ret_candi);
                continue;
            } else {
                ret_candi = 1;
                continue;
            }
        }

        return ret;
    }
};