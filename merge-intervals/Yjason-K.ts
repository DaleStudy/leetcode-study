/**
 * 겹치는 구간(interval)을 병합하는 함수
 * @param {number[][]} intervals - 각 구간을 나타내는 2차원 배열 [[start, end], ...]
 * @returns {number[][]} - 겹치는 구간을 병합한 결과 배열
 *
 * 시간 복잡도: O(n log n)
 *  - 정렬 과정에서 O(n log n), 병합 과정에서 O(n)으로 최종 O(n log n)
 *
 * 공간 복잡도: O(n)
 *  - 정렬된 배열을 저장하는 데 O(n), 결과 배열도 O(n)을 차지
 */
function merge(intervals: number[][]): number[][] {
    let result: number[][] = [];
    
    // 시작 시간을 기준으로 정렬 (오름차순)
    intervals.sort((a, b) => a[0] - b[0]);

    for (let interval of intervals) {
        // 결과 리스트가 비어있거나
        // 현재 구간이 이전 구간과 겹치지 않는 경우
        if (result.length === 0 || result[result.length - 1][1] < interval[0]) {
            result.push(interval); // 새로운 구간 추가
        } else {
            // 결과 값의 마지막 interval을 기준으로
            // 현재 구간이 이전 구간과 겹치는 경우, 두 구간을 병합
            result[result.length - 1][1] = Math.max(result[result.length - 1][1], interval[1]);
        }
    }

    return result;
}

