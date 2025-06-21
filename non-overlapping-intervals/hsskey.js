/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    let res = 0;
    let prevEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];

        if (start >= prevEnd) {
            prevEnd = end;
        } else {
            res += 1;
            prevEnd = Math.min(end, prevEnd);
        }
    }

    return res;
};

