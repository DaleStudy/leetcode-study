/**
 * 문제 설명
 * - 겹치지 않는 최대한 많은 구간을 선택하는 문제 (그러기 위해서는 몇개를 제거해야하는지)
 *
 * 아이디어
 * 1) 그리디 알고리즘
 *   - 최대한 많은 구간 선택을 위해서는 끝나는 시간을 기준으로 정렬
 *   - 순회 하면서 다음 시작 시간이 현재 끝나는 시간보다 크거나 같으면 카운트 증가
 */
function eraseOverlapIntervals(intervals: number[][]): number {
  if (intervals.length === 0) return 0;

  intervals.sort((a, b) => a[1] - b[1]);

  let count = 1;
  let end = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] >= end) {
      count++;
      end = intervals[i][1];
    }
  }
  return intervals.length - count;
}
