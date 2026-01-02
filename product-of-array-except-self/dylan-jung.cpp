class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        ans.resize(nums.size(), 1);
        int p = 1;
        int idx = nums.size()-1;
        for(auto it = nums.rbegin(); it != nums.rend(); it++, idx--) {
            ans[idx] *= p;
            p *= *it; // 마지막 건 그냥 무시
        }
        p = 1;
        idx = 0;
        for(auto it = nums.begin(); it != nums.end(); it++, idx++) {
            ans[idx] *= p;
            p *= *it;
        }
        return ans;
    }
};
