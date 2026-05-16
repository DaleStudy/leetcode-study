class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // start 순으로 정렬
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });

        vector<vector<int>> res;
        res.reserve(intervals.size());

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1; i < intervals.size(); ++i) 
        {
            // 현재 구간의 end보다 start가 크다면 틈이 벌어진 것
            if (end < intervals[i][0])
            {
                vector<int> v = { start, end };
                res.push_back(v);
                start = intervals[i][0];
                end = intervals[i][1];
            }
            // 그렇지 아니면 합칠 수 있음
            else
            {
                start = min(start, intervals[i][0]);
                end = max(end, intervals[i][1]);
            }
        }

        vector<int> v = { start, end };
        res.push_back(v);

        return res;
    }
};
