// 1) Sort -> val, cnt -> 
// T(C) : O(NlogN)
// 2) Heap
// T(C) : O(NlogN)
// 3) Bucket Sort
// T(C) : O(N)
class Solution {
private:
    struct Node
    {
        int val;
        int cnt;
        bool operator<(const Node &input) const 
        {
            return cnt < input.cnt;
        }
    };
public:
    // Solution 2 - Heap
    // vector<int> topKFrequent(vector<int>& nums, int k) {
    //     priority_queue<Node> pq;
    //     unordered_map<int, int> numCnt;
    //     vector<int> topKvalueVec;
    //     for(auto num : nums)
    //         numCnt[num] += 1;
    //     for(auto it : numCnt)
    //         pq.push({it.first, it.second});
    //     for (int i = 0; i < k && !pq.empty(); i++)
    //     {
    //         topKvalueVec.push_back(pq.top().val);
    //         pq.pop();
    //     }
    //     return topKvalueVec;
    // }
    
    // Solution 3 - Bucket Sort
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> numToCnt;
        vector<vector<int>> freq(nums.size() + 1, vector<int>());
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++)
            numToCnt[nums[i]] += 1;
        for (auto it : numToCnt)
            freq[it.second].push_back(it.first);
        for (int cnt = nums.size(); cnt >= 0; cnt--)
        {
            for (auto num : freq[cnt])
            {
                ans.push_back(num);
                if (ans.size() >= k)
                    return ans;
            }
        }
        return ans;
    }
};
