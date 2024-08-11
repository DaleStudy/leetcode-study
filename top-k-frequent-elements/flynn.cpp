/**
 * For given size of nums N and K,
 * 
 * Time complexity: O(N + MlogM + KlogM) <= O(NlogN)
 *   - the first iteration: O(N)
 *     - N times of 
 *     - unordered_map find: O(1) on average
 *     - unordered_map insert: O(1) on average
 *   - the second iteration: O(MlogM) such that M is the number of unique numbers
 *     - M times of
 *     - priority_queue push: O(logM)
 *   - the last iteration of making result: O(KlogM)
 *     - K times of
 *     - priority_queue pop: O(logM)
 * 
 *  Space complexity: O(N) at worst
 */

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        priority_queue<pair<int, int>> pq;
        unorderd_map<int, int> m;

        auto nums_it = nums.begin();
        while (nums_it != nums.end()) {
            if (m.find(*nums_it) == m.end()) m.insert({*nums_it, 1});
            else m[*nums_it]++;
            nums_it++;
        }

        auto m_it = m.begin();
        while (m_it != m.end()) {
            pq.push({(*m_it).second, (*m_it).first});
            m_it++;
        }

        while (k--) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};