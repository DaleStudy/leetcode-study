class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    bool canAttendMeetings(vector<Interval> &intervals) {
        // 시작 시간 기준으로 정렬
        sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b) {
            return a.start < b.start;
        });

        // 시작시간과 끝시간을 비교해서 겹치면 false 반환
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i].start < intervals[i - 1].end) {
                return false;
            }
        }
        return true;
    }
};
