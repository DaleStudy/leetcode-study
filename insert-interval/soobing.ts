/**
 * 문제 설명
 * - 주어진 시간 간격에 대해 회의를 참석할 수 있는지 여부를 반환하는 문제
 *
 * 아이디어
 * 1) 시작 시간을 기준으로 정렬 후, 이전 회의의 종료 시간과 현재 회의의 시작 시간을 비교하여 참석 가능 여부를 판단
 *
 */

function insert(intervals: number[][], newInterval: number[]): number[][] {
  const result: number[][] = [];
  let i = 0;

  while (i < intervals.length && newInterval[0] > intervals[i][1]) {
    result.push(intervals[i]);
    i++;
  }

  while (i < intervals.length && newInterval[1] >= intervals[i][0]) {
    newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
    newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
    i++;
  }
  result.push(newInterval);

  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }

  return result;
}
