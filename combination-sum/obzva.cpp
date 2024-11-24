class Solution {
public:
vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
vector<vector<int>> res;
queue<pair<int, pair<int, vector<int>>>> q; // {acc, {idx, combination}}

        for (int i = 0; i < candidates.size(); i++) {
            int num = candidates[i];

            if (num <= target) {
                vector<int> comb;
                comb.push_back(num);
                q.push({num, {i, comb}});
            }

        }

        while (!q.empty()) {
            auto p = q.front();
            q.pop();

            int acc = p.first, idx = p.second.first;
            auto comb = p.second.second;

            if (acc == target) {
                res.push_back(comb);
            } else if (acc < target) {
                for (int i = idx; i < candidates.size(); i++) {
                    int num = candidates[i];

                    if (acc + num <= target) {
                        vector<int> new_comb(comb);
                        new_comb.push_back(num);
                        q.push({acc + num, {i, new_comb}});
                    }
                }
            }
        }

        return res;
    }

};
