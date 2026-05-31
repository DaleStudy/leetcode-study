class Solution {
public:
    vector<vector<int>> ans;
    vector<int> candids;
    int t;

    void dfs(int idx, int sum, vector<int> s) {
        if(sum > t) return;
        else if (sum == t) ans.push_back(s);

        for(int i = idx; i < candids.size(); i++) {
            auto next = vector<int>(s);
            next.push_back(candids[i]);
            dfs(i, sum+candids[i], next);
        }
    };

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        candids = candidates;
        t = target;
        dfs(0, 0, {});
        return ans;
    }
};
