/**
 * https://leetcode.com/problems/insert-interval/submissions/1678158074/
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  const result = [];
  let i = 0;
  const n = intervals.length;

  // 1. newInterval보다 끝나는 시점이 먼저인 interval은 그냥 추가
  while (i < n && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }

  // 2. newInterval과 겹치는 interval은 병합
  while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  result.push(newInterval);

  // 3. 나머지 interval은 그대로 추가
  while (i < n) {
    result.push(intervals[i]);
    i++;
  }

  return result;
};
