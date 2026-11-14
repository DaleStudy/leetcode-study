// n: number of elements, m: number of distinct values
// Time Complexity: O(n + m log m) on average
// Space Complexity: O(m)

#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        for(int n: nums) freq[n]++;

        vector<pair<int, int>> v(freq.begin(), freq.end());
        sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        vector<int> res;
        for(int i = 0; i < k; i++)
            res.push_back(v[i].first);

        return res;
    }
};
