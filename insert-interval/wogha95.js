/**
 * TC: O(N)
 * 1번에서 N만큼 순회
 * 2번에서 최대 N만큼 순회
 *
 * SC: O(1)
 * 겹치는 interval의 시작, 끝 index를 저장하는 변수만 사용
 *
 * N: intervals.length
 */

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
  if (intervals.length === 0) {
    return [newInterval];
  }
  if (newInterval[1] < intervals[0][0]) {
    return [newInterval, ...intervals];
  }
  if (intervals[intervals.length - 1][1] < newInterval[0]) {
    return [...intervals, newInterval];
  }

  // 1. 겹치는 interval의 시작, 끝 index를 구한다.
  let overLappingStartIndex = intervals.length - 1;
  let overLappingEndIndex = 0;
  for (let index = 0; index < intervals.length; index++) {
    const interval = intervals[index];
    if (
      (interval[0] <= newInterval[0] && newInterval[0] <= interval[1]) ||
      newInterval[0] < interval[0]
    ) {
      overLappingStartIndex = Math.min(overLappingStartIndex, index);
    }
    if (
      (interval[0] <= newInterval[1] && newInterval[1] <= interval[1]) ||
      interval[1] < newInterval[1]
    ) {
      overLappingEndIndex = Math.max(overLappingEndIndex, index);
    }
  }

  // 2.
  // 시작index 전까지 모두 추가하고
  // 시작index, 끝index의 최대 범위 interval을 추가하고
  // 끝index 이후 interval을 모두 추가한다.
  const result = [];
  for (let index = 0; index < overLappingStartIndex; index++) {
    result.push(intervals[index]);
  }
  const overLappedStart = Math.min(
    intervals[overLappingStartIndex][0],
    newInterval[0]
  );
  const overLappedEnd = Math.max(
    intervals[overLappingEndIndex][1],
    newInterval[1]
  );
  result.push([overLappedStart, overLappedEnd]);
  for (let index = overLappingEndIndex + 1; index < intervals.length; index++) {
    result.push(intervals[index]);
  }

  return result;
};
