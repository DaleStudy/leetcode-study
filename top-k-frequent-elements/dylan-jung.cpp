class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        map<int, vector<int>> freq;
        for(auto i: nums) m[i] += 1;
        for(auto item: m) {
            auto [k, v] = item;
            freq[v].push_back(k);
        }

        vector<int> ans;
        ans.reserve(k);
        auto it = freq.rbegin();
        while(k > 0) {
            auto kth = it->second;
            ans.insert(ans.end(), kth.begin(), kth.end());
            k-=kth.size();
            it++;
        }
        return ans;
    }
};
