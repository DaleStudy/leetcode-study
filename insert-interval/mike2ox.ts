/**
 * Source: https://leetcode.com/problems/insert-interval/
 * 풀이방법: 미리 정렬 후 끝 부분만 비교하면서 갱신시키기
 * 시간복잡도: O(nlogn) - 정렬때문에
 * 공간복잡도: O(n)
 *
 * 통과시간
 * - 최초: 40분
 */
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const mergedIntervals = [...intervals, newInterval];
  const result: number[][] = [];
  mergedIntervals.sort((a, b) => a[0] - b[0]);

  for (const interval of mergedIntervals) {
    // 결과 배열이 비어있거나 현재 구간이 마지막 구간과 겹치지 않는 경우
    if (result.length === 0 || interval[0] > result[result.length - 1][1]) {
      result.push(interval);
    } else {
      // 결과물의 마지막 구간의 큰값 범위와 현재 구간의 큰값 범위를 비교후 큰 값으로 대체하기
      result[result.length - 1][1] = Math.max(
        result[result.length - 1][1],
        interval[1]
      );
    }
  }

  return result;
}
