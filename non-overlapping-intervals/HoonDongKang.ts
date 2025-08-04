/**
 * [Problem]: [435] Non-overlapping Intervals
 * (https://leetcode.com/problems/non-overlapping-intervals/description/)
 */

//시간복잡도 O(n log n)
//공간복잡도 O(1)
function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);

    let count = 0;
    let prev = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        let [start, end] = intervals[i];

        if (prev > start) {
            count++;
        } else {
            prev = end;
        }
    }

    return count;
}
