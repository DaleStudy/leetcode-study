/**
 * [Problem]: [919] Meeting Rooms II
 * (https://www.lintcode.com/problem/919/)
 */

export class Interval {
    start: number;
    end: number;
    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    }
}

// 시간복잡도 O(n log n)
// 공간복잡도 O(n)
export class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    minMeetingRooms(intervals: Interval[]): number {
        if (intervals.length === 0) return 0;

        const starts = intervals.map((i) => i.start).sort((a, b) => a - b);
        const ends = intervals.map((i) => i.end).sort((a, b) => a - b);

        let count = 0;
        let maxCount = 0;
        let endIdx = 0;

        for (let i = 0; i < intervals.length; i++) {
            if (starts[i] < ends[endIdx]) {
                count++;
            } else {
                endIdx++;
            }

            maxCount = Math.max(maxCount, count);
        }

        return maxCount;
    }
}
