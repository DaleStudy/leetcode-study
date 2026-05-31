class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        queue<pair<int, vector<int>>> que;
        vector<int> comb;
        int sum, num;

        sort(candidates.begin(), candidates.end());

        for(int i = 0; i < candidates.size(); i++) {
            num = candidates[i];
            if(num > target)  
                continue;
            que.push({num, vector<int> ({num})});
        }

        while(!que.empty()) {
            sum = que.front().first;
            comb = que.front().second;
            que.pop();
            
            if(sum == target) {
                ans.push_back(comb);
                continue;
            }

            for(int i = 0; i < candidates.size(); i++) {
                num = candidates[i];
                if(sum + num <= target && comb[comb.size() - 1] <= num) {
                    comb.push_back(num);
                    que.push({sum + num, comb});
                    comb.pop_back();
                }
            }
        }

        return ans;
    }
};

