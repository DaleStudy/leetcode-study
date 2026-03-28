class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> v;
    
        solve(candidates, target, v, 0, res, 0);
        return res;
    }

    /**
     * @param candidates    사용할 수 있는 수의 후보
     * @param target        candidates의 원소들을 사용해 만들어야하는 합계
     * @param cur           지금까지 시도한 조합
     * @param sum           사전에 계산된 cur 원소들의 합계
     * @param res           최종 결과
     * @param idx           현재까지 진행된 인덱스 (중복 방지를 위해 존재)
     */
    void solve(const vector<int>& candidates, const int target, vector<int>& cur, int sum, vector<vector<int>>& res, int idx)
    {
        if (sum > target)
        {
            return;
        }

        if (sum == target)
        {
            res.push_back(cur);
            return;
        }

        int len = candidates.size();
        for (int i = idx; i < len; ++i)
        {
            int c = candidates[i];
            cur.push_back(c);
            solve(candidates, target, cur, sum + c, res, i);
            cur.pop_back();
        }
    }
};
