/*
Time complexity: O(nlogn)
Space complexity: O(n)
*/
function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1])
    let cnt = 0
    let end = intervals[0][1]
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < end) {
            cnt++
        } else {
            end = intervals[i][1]
        }
    }
    return cnt
};
