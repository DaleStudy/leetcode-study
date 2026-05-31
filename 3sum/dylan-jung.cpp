class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int a = 0; a < nums.size()-2; a++) {
            if (a > 0 && nums[a] == nums[a - 1]) continue;
            int b = a + 1;
            int c = nums.size() - 1;
            while(b < c) {
                if(nums[a] + nums[b] + nums[c] < 0) {
                    b++;
                }
                else if (nums[a] + nums[b] + nums[c] > 0) {
                    c--;
                }
                else {
                    result.push_back({nums[a], nums[b], nums[c]});
                    b++;
                    c--;
                    while (b < c && nums[b] == nums[b - 1]) b++;
                    while (b < c && nums[c] == nums[c + 1]) c--;
                }
            }
        }

        return result;
    }
};
