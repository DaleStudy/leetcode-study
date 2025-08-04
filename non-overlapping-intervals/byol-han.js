/**
 * https://leetcode.com/problems/non-overlapping-intervals/description/
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  if (intervals.length === 0) return 0;

  // 1. intervals를 end 값을 기준으로 오름차순 정렬
  intervals.sort((a, b) => a[1] - b[1]);

  // 2. 첫 번째 interval의 end 값으로 초기화
  let end = intervals[0][1];
  let count = 0; // 제거해야 하는 interval의 개수

  // 3. 두 번째 interval부터 순회
  for (let i = 1; i < intervals.length; i++) {
    let [start_i, end_i] = intervals[i];

    if (start_i < end) {
      // 현재 interval의 start가 이전 end보다 작으면 overlap
      count++; // 이 interval은 제거해야 함
    } else {
      // overlap이 없으면 end 갱신
      end = end_i;
    }
  }

  return count;
};
