#include <bits/stdc++.h>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) 
            return 0;

        sort(nums.begin(), nums.end());

        int ans = 1, cnt = 1;
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] == nums[i - 1])
                continue;
            if(nums[i] - 1 == nums[i - 1])
                cnt++;
            else
                cnt = 1;
            ans = max(cnt, ans);
        }

        return ans;
    }
};

