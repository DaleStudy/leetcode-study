class Solution {
public:
    // int missingNumber(vector<int>& nums) {
    //     sort(nums.begin(), nums.end());

    //     for(int i = 0; i < nums.size(); i++)
    //         if(i != nums[i])
    //             return i;

    //     return nums.size();
    // }

    // int missingNumber(vector<int>& nums) {
    //     int ans = nums.size();
    //     for(int i = 0; i < nums.size(); i++)
    //         ans ^= i ^ nums[i];
    //     return ans;
    // }

    int missingNumber(vector<int>& nums) {
        int idx = 0;
        while(idx < nums.size()) {
            int val = nums[idx];
            if(val <  nums.size() && val != idx)
                swap(nums[idx], nums[val]);
            else
                idx++;
        }

        for(int i = 0; i < nums.size(); i++)
            if(i != nums[i])
                return i;

        return nums.size();
    }
};

