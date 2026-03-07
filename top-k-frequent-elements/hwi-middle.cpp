class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for(auto n : nums) 
        {
            ++m[n];
        }

        vector<pair<int, int>> v(m.begin(), m.end());
        sort(v.begin(), v.end(), [](const auto& a, const auto& b)
        {
            return a.second > b.second;
        });

        vector<int> ans;
        ans.reserve(k);
        for (int i = 0; i < k; ++i)
        {
            ans.push_back(v[i].first);
        }
        return ans;
    }
};
