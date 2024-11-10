/**
 * https://www.lintcode.com/problem/920/
 * time complexity : O(n log n)
 * space complexity : O(log n)
 */

export class Interval {
    start: number;
    end: number;
    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    }
}
g
export function canAttendMeetings(intervals: Interval[]): boolean {
    intervals.sort((a, b) => a.start - b.start);

    for (let i = 0; i < intervals.length - 1; i++) {
        const { end } = intervals[i];
        const { start: nextStart } = intervals[i + 1];

        if (end > nextStart) return false;
    }
    return true;
}
