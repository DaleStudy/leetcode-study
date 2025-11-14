#include <bits/stdc++.h>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> num_idx;
        for(int i = 0; i < nums.size(); i++)
            num_idx.push_back({nums[i], i});
        
        sort(num_idx.begin(), num_idx.end());

        int left = 0, right = nums.size() - 1;
        while(1) {
            if (num_idx[left].first + num_idx[right].first == target)
                return vector<int>({num_idx[left].second, num_idx[right].second});
            if(num_idx[left].first + num_idx[right].first < target) left++;
            else right--;
        }
    }
};

