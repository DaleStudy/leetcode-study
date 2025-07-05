export class Solution {
    /**
     * @param {Interval[]} intervals - an array of meeting time intervals
     * @return {number} the minimum number of conference rooms required
     */
    minMeetingRooms(intervals) {
        if (!intervals || intervals.length === 0) return 0;

        const start = intervals.map(i => i.start).sort((a, b) => a - b);
        const end = intervals.map(i => i.end).sort((a, b) => a - b);

        let res = 0;
        let count = 0;
        let s = 0,
            e = 0;

        while (s < intervals.length) {
            if (start[s] < end[e]) {
                s += 1;
                count += 1;
            } else {
                e += 1;
                count -= 1;
            }
            res = Math.max(res, count);
        }

        return res;
    }
}

