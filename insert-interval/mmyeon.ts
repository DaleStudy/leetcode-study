/**
 *@link https://leetcode.com/problems/insert-interval/description/
 *
 * 접근 방법 :
 *  - 새로운 interval을 기존 interval에 추가하고, 시작 지점 기준으로 오름차순 정렬
 *  - 현재 interval이 result의 마지막 interval과 겹치는 경우, 종료 지점 업데이트해서 병함
 *  - 겹치지 않으면, result 배열에 현재 interval 추가
 *
 * 시간복잡도 : O(nlogn)
 *  - n = intervals 개수
 *  - 오름차순으로 정렬
 *
 * 공간복잡도 : O(n)
 *  - n = 병합 후 result 배열에 담긴 인터벌의 개수
 */
function insert(intervals: number[][], newInterval: number[]): number[][] {
  const sortedIntervals = [...intervals, newInterval].sort(
    (a, b) => a[0] - b[0]
  );
  const result: number[][] = [sortedIntervals[0]];

  for (let i = 1; i < sortedIntervals.length; i++) {
    const lastInterval = result[result.length - 1];
    const currentInterval = sortedIntervals[i];

    if (currentInterval[0] <= lastInterval[1]) {
      lastInterval[1] = Math.max(currentInterval[1], lastInterval[1]);
    } else {
      result.push(currentInterval);
    }
  }

  return result;
}
