/**
 * @link https://leetcode.com/problems/merge-intervals/
 *
 * 접근 방법 :
 *  - 인터벌 배열 첫 번째 요소 기준으로 오름차순 정렬
 *  - 인터벌의 시작이 이전 인터벌 끝보다 작으면 범위 업데이트
 *  - 범위에 속하지 않으면 현재 인터벌을 결과 배열에 추가하고 새로운 인터벌로 업데이트
 *
 * 시간복잡도 : O(nlogn)
 *  - n = 인터벌 배열의 길이
 *  - 인터벌 배열 정렬 : O(nlogn)
 *  - 병합 과정: O(n)
 *
 * 공간복잡도 : O(n)
 *  - 결과 배열에 담아서 리턴
 */
function merge(intervals: number[][]): number[][] {
  const result: number[][] = [];

  if (intervals.length < 2) return intervals;

  // 첫번째 요소 기준으로 정렬
  const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);

  let [start, end] = sortedIntervals[0];

  for (let i = 1; i < sortedIntervals.length; i++) {
    const [newStart, newEnd] = sortedIntervals[i];
    if (newStart <= end) {
      // 범위 겹치는 경우, end 업데이트
      end = Math.max(end, newEnd);
    } else {
      // 겹치지 않는 경우, 현재 구간 추가하고 새로운 구간으로 업데이트
      result.push([start, end]);
      [start, end] = [newStart, newEnd];
    }
  }

  // 마지막 구간 추가
  result.push([start, end]);

  return result;
}
