/*
Time Complexity: O(n)
Space Complexity: O(n)
*/
function insert(intervals: number[][], newInterval: number[]): number[][] {
    const newIntervals = []
    let idx = 0
    const n = intervals.length
    while (idx < n && intervals[idx][1] < newInterval[0]) {
        newIntervals.push(intervals[idx])
        idx++
    }

    while (idx < n && intervals[idx][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[idx][0])
        newInterval[1] = Math.max(newInterval[1], intervals[idx][1])
        idx++
    }
    newIntervals.push(newInterval)

    while (idx < n) {
        newIntervals.push(intervals[idx])
        idx++
    }
    return newIntervals
};
