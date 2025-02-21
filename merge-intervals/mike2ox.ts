/**
 * Source: https://leetcode.com/problems/merge-intervals/
 * 풀이방법: 정령후 첫번째 구간 추가하고 이후 순회하면서 겹치는지 확인 후 병합 or 추가
 * 시간복잡도: O(NlogN) - 정렬에서 NlogN
 * 공간복잡도: O(N) - 결과 저장할 공간
 */

function merge(intervals: number[][]): number[][] {
  if (intervals.length <= 1) return intervals;

  intervals.sort((a, b) => a[0] - b[0]);
  const result: number[][] = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const current = intervals[i];
    const lastMerged = result[result.length - 1];

    // 현재 구간의 시작점이 이전 구간의 끝점보다 작거나 같으면 merge
    if (current[0] <= lastMerged[1]) {
      lastMerged[1] = Math.max(lastMerged[1], current[1]); // 끝점을 두 구간의 끝점 중 더 큰 값으로 업데이트
    } else {
      result.push(current);
    }
  }

  return result;
}
