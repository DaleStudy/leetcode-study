/**
 * 문제 설명
 * - 주어진 배열의 구간을 병합하는 문제
 *
 * 아이디어
 * 1) 그리디 알고리즘
 *   - 시작점 기준으로 배열을 정렬
 *   - 결과를 담을 merge 배열을 만들고, 첫 번째 구간을 추가한다. 그리고 비교는 두번재 구간부터 순차적으로 진행
 *   - 머지된 마지막 구간의 끝보다 현재 구간의 시작점이 작을 경우 머지를 진행하고, 아닌 경우는 머지 배열에 추가한다.
 */
function merge(intervals: number[][]): number[][] {
  if (intervals.length === 0) return [];

  intervals.sort((a, b) => a[0] - b[0]);

  const merged: number[][] = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const lastMerged = merged[merged.length - 1];
    const current = intervals[i];
    if (current[0] <= lastMerged[1]) {
      lastMerged[1] = Math.max(current[1], lastMerged[1]);
    } else {
      merged.push(current);
    }
  }
  return merged;
}
