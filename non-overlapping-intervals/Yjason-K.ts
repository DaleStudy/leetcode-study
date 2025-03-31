/**
 * 주어진 interval 배열에서 구간이 서로 겹치지 않기 위해서 제거해야 하는 최소한의 interval 수 구하기. 
 * @param {number[][]} intervals - interval 정보를 담는 2차원 배열 [start, end][]
 * @returns {number} -  제거한 interval 최소 개수
 */
function eraseOverlapIntervals(intervals: number[][]): number {
    // interval의 end 기준으로 정렬
    intervals.sort((a, b) => a[1] - b[1]);

    // 제거해야 하는 interval 수
    let result = 0;
    //  비교할 기준 interval
    let prevInterval = intervals[0];

    // 0 idx를 기준으로 하기 때문에 1번 idx부터 비교
    for(let i=1; i < intervals.length; i++) {
        // 이전 idx와 비교할 interval이 겹치는 경우
        if(intervals[i][0]  < prevInterval[1]) {
            result++;
        } else {
            // 겹치치 않는경우 기준 interval 변경
            prevInterval = intervals[i];
        }
    }
 

    return result;
}

