// Time Complexity: O(n) on average
// Space Complexity: O(n)

#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int n: nums) freq[n]++;

        vector<vector<int>> bucket(nums.size() + 1);
        for (auto& [num, f]: freq) bucket[f].push_back(num);


        vector<int> res;
        for (int f = nums.size(); f >= 1 && res.size() < k; f--)
            for (int n: bucket[f]) res.push_back(n);

        return res;
    }
};
