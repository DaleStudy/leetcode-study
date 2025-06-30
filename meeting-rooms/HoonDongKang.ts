/**
 * [Problem]: [920] Meeting Rooms
 * (https://www.lintcode.com/problem/920/)
 */

export class Interval {
    start: number;
    end: number;
    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    }
}

export class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    canAttendMeetings(intervals: Interval[]): boolean {
        //시간복잡도 O(n^2)
        //공간복잡도 O(1)
        function bruteForceFunc(intervals: Interval[]): boolean {
            for (let i = 0; i < intervals.length; i++) {
                for (let j = i + 1; j < intervals.length; j++) {
                    const first = intervals[i];
                    const second = intervals[j];
                    if (first.start < second.end && second.start < first.end) {
                        return false;
                    }
                }
            }

            return true;
        }

        //시간복잡도 O(nlogn)
        //공간복잡도 O(1)
        function sortedFunc(intervals: Interval[]): boolean {
            intervals.sort((a, b) => a.start - b.start);

            for (let i = 0; i < intervals.length - 1; i++) {
                if (intervals[i].end > intervals[i + 1].start) {
                    return false;
                }
            }

            return true;
        }
    }
}
