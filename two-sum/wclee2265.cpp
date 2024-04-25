// https://leetcode.com/problems/two-sum/
// Time Complexity : O(nlogn)
// Space Complexity : O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<pair<int, int> > numsIndices;

        for(int i=0; i<n; i++){
            numsIndices.push_back({nums[i], i});
        }

        sort(numsIndices.begin(), numsIndices.end());
        int i, j = n-1;
        for(i=0; i<n; i++) {
            while(numsIndices[i].first + numsIndices[j].first > target) j--;
            if(numsIndices[i].first + numsIndices[j].first == target) break;
        }

        vector<int> ans;
        ans.push_back(numsIndices[i].second);
        ans.push_back(numsIndices[j].second);
        return ans;
    }
};
