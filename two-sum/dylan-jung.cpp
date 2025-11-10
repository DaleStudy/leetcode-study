class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<tuple<int, int>> arr;
        arr.reserve(nums.size());
        for(int i = 0; i < nums.size(); i++) {
            arr.push_back({nums[i], i});
        }
        int s = 0; int e = nums.size()-1;
        sort(arr.begin(), arr.end());
        while(s < e) {
            if(get<0>(arr[s]) + get<0>(arr[e]) > target) e-=1;
            else if (get<0>(arr[s]) + get<0>(arr[e]) < target) s+=1;
            else return {get<1>(arr[s]), get<1>(arr[e])};
        }
        return {};
    }
};
