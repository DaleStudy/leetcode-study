/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
const insert = function(intervals, newInterval) {
    const merged = [];
    let i = 0;

    // 겹치지 않는 앞부분 push
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
        merged.push(intervals[i]);
        i++;
    }

    // 겹치는 부분 처리
    while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    merged.push(newInterval);

    // 겹치지 않는 뒷부분 push
    while (i < intervals.length) {
        merged.push(intervals[i]);
        i++;
    }

    return merged;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n) (반환할 배열)
