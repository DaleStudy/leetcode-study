class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        // 끝나는 시간을 기준으로 정렬
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) { return a[1] < b[1]; });

        int count = 1; // 첫 구간은 항상 선택
        int end = intervals[0][1]; // 첫 구간의 끝

        for (int i = 1; i < intervals.size(); i++) {
            // 현재 구간이 겹치지 않으면 선택
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }

        // 제거해야 하는 구간 수 = 전체 - 선택된 개수
        return intervals.size() - count;
    }
};
