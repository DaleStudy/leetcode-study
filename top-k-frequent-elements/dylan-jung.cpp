// TC: O(N), SC: O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        freq.reserve(nums.size() * 2);
        for (int x : nums) {
            ++freq[x];
        }

        int n = nums.size();
        vector<vector<int>> bucket(n + 1);
        for (auto& p : freq) {
            int num = p.first;
            int cnt = p.second;
            bucket[cnt].push_back(num);
        }

        vector<int> ans;
        ans.reserve(k);
        
        for (int count = n; count >= 1 && ans.size() < k; --count) {
            for (int num : bucket[count]) {
                ans.push_back(num);
                if (ans.size() == k) break;
            }
        }

        return ans;
    }
};
