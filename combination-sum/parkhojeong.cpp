// N = candidates.size(), T = target, M = min(candidates)
// Time: O(N^(T/M)), Space: O(T/M)
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> answer;
        vector<int> path;

        function<void(int, int)> recur = [&](int start, int remain) {
            if (remain == 0) {
                answer.push_back(path);
                return;
            }
            for (int i = start; i < candidates.size(); i++) {
                if (candidates[i] > remain) break;
                path.push_back(candidates[i]);
                recur(i, remain - candidates[i]);
                path.pop_back();
            }
        };

        recur(0, target);
        return answer;
    }
};
