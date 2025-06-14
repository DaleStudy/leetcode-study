/*
Time complexity: O(NlogN)
Space complexity: O(N)
*/
function merge(intervals: number[][]): number[][] {
    if (intervals.length === 0) return intervals
    intervals.sort((a, b) => a[0] - b[0])
    const result = []
    for (const interval of intervals) {
        if (result.length === 0 || result[result.length - 1][1] < interval[0]) {
            result.push(interval)
        } else {
            result[result.length - 1][1] = Math.max(result[result.length -1][1], interval[1])
        }
    }
    return result
};
