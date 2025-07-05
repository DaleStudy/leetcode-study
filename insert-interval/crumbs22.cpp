class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int i = 0;

        // 겹치지 않을 때 res 벡터에 intervals를 그대로 삽입
        while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
            res.push_back(intervals[i]);
            i++;
        }

        // 겹치는 동안 반복하며 시작지점과 끝지점 갱신
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.push_back(newInterval); // 삽입

        // 남은 벡터 마저 삽입
        while (i < intervals.size()) {
            res.push_back(intervals[i]);
            i++;
        }
        return (res);
    }
};
