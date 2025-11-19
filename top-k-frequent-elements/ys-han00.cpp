#include <bits/stdc++.h>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> count;

        for(int i = 0; i < nums.size(); i++) {
            if(count.find(nums[i]) == count.end())
                count[nums[i]] = 1;
            else
                count[nums[i]]++;
        }

        vector<pair<int, int>> cnt(count.begin(), count.end());
        sort(cnt.begin(), cnt.end(), cmp);

        vector<int> ans;
        for(int i = 0; i < k; i++)
            ans.push_back(cnt[i].first);
        
        return ans;
    }

    static bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
    }
};

