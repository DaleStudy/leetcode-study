/**
 *@link https://leetcode.com/problems/non-overlapping-intervals/description/
 *
 * 접근 방법 :
 *  - 최소 삭제 횟수를 구하기 위해서 인터벌 종료 시점이 빠른 걸 기준으로 정렬
 *  - 탐색 범위를 좁히기 위해서 이전 인터벌 범위와 비교 -> 이전 인터벌 종료 지점보다 시작점이 빠르면 포함되어 있으면 겹치니까 삭제 카운트 증가
 *  - 겹치지 않을 때는 이전 인터벌을 현재 인터벌로 업데이트하기
 *
 * 시간복잡도 : O(nlogn)
 *  - n = intervals의 길이
 *  - 정렬했으므로 O(nlogn)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 */
function eraseOverlapIntervals(intervals: number[][]): number {
  intervals.sort((a, b) => a[1] - b[1]);

  let eraseCount = 0,
    previousInterval = intervals[0];

  for (let i = 1; i < intervals.length; i++) {
    const currentInterval = intervals[i];

    if (currentInterval[0] < previousInterval[1]) {
      eraseCount++;
    } else {
      previousInterval = intervals[i];
    }
  }

  return eraseCount;
}
