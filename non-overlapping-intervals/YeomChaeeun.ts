
/**
 * 알고리즘 복잡도
 * - 시간 복잡도: O(nlogn)
 * - 공간 복잡도: O(1)
 */
function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]) 
    let end = intervals[0][1]
    let count = 0
    for(let i = 1; i < intervals.length; i++) {
        if(intervals[i][0] < end) {
            count++
        } else {
            end = intervals[i][1]
        }
    }
    return count
}
