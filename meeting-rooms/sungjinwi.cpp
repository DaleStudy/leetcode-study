/*
    풀이 : 
        시작 시간 기준으로 intervals 정렬 후 반복문 돌면서 옆 구간과 겹치는 구간이 있으면 false 모두 안 겹치면 true
    
    intervals 개수 : N

    TC : O (N log N)
        정렬 시간복잡도

    SC : O (1)
*/

#include <vector>
#include <algorithm>

using namespace std;

/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
    public:
        /**
         * @param intervals: an array of meeting time intervals
         * @return: if a person could attend all meetings
         */
        bool canAttendMeetings(vector<Interval> &intervals) {
            sort(intervals.begin(), intervals.end(), [] (Interval& a, Interval& b) {return a.start <= b.start;});
            for (int i = 0; i < intervals.size() - 1; i++) {
                if (intervals[i].end > intervals[i + 1].start)
                    return false;
            }
            return true;
        }
    };
