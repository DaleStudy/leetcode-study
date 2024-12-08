class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mp;
        priority_queue<pair<int, int>> pq;
        vector<int> ans;

        for(auto b : nums) mp[b]++;

        for(auto p : mp) pq.push({p.second, p.first});

        while(k--)ans.push_back(pq.top().second), pq.pop();

        return ans;
    }
};
