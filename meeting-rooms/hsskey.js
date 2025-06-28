import {
    Interval,
} from '/opt/node/lib/lintcode/index.js';

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

export class Solution {
    /**
     * @param {Interval[]} intervals - an array of meeting time intervals
     * @return {boolean} - whether a person could attend all meetings
     */
    canAttendMeetings(intervals) {
        // start 기준으로 정렬
        intervals.sort((a, b) => a.start - b.start);

        // 연속된 회의의 시간 비교
        for (let i = 1; i < intervals.length; i++) {
            const prev = intervals[i - 1];
            const curr = intervals[i];

            if (prev.end > curr.start) {
                return false;
            }
        }

        return true;
    }
}
