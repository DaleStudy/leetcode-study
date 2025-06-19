/**
 * 구간이 겹치지 않게 하기 위해 최소한의 구간을 없애야 할 때, 몇 개를 없애야 하는지 반환하는 함수
 * @param {number[][]} intervals
 * @return {number}
 */
const eraseOverlapIntervals = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0]);
    
    let count = 0;
    let prevEnd = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];

        // 범위가 겹치는 경우
        if (prevEnd > start) {
            count++;
            prevEnd = Math.min(prevEnd, end); // end가 큰 걸 삭제한다 치기
        }
    }
    
    return count;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
