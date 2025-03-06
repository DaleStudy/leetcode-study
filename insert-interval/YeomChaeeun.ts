/**
 * 중간에 새로운 구간 추가하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param intervals
 * @param newInterval
 */
function insert(intervals: number[][], newInterval: number[]): number[][] {
    if(intervals.length === 0) return [newInterval]
    let result: number[][] = []

    let i = 0;

    // 1. newIntervals 이전 구간 추가
    while(i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i])
        i++
    }

    // 2. 겹치는 부분 추가
    const merged = [...newInterval]
    while(i < intervals.length && intervals[i][0] <= newInterval[1]) {
        merged[0] = Math.min(merged[0], intervals[i][0])
        merged[1] = Math.max(merged[1], intervals[i][1])
        i++
    }
    result.push(merged)

    // 3. 이후의 구간 추가
    while(i < intervals.length) {
        result.push(intervals[i])
        i++
    }

    return result
}

