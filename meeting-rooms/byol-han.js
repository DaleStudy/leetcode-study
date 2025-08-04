import { Interval } from '/opt/node/lib/lintcode/index.js';

/**
 * https://www.lintcode.com/problem/920/
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
    // 먼저 회의를 시작 시간 기준으로 정렬합니다.
    intervals.sort((a, b) => a[0] - b[0]);

    // 정렬된 회의들을 순차적으로 비교하며 겹치는지 확인합니다.
    for (let i = 1; i < intervals.length; i++) {
      const prevEnd = intervals[i - 1][1]; // 이전 회의의 끝 시간
      const currStart = intervals[i][0]; // 현재 회의의 시작 시간

      // 이전 회의의 끝 시간보다 현재 회의의 시작 시간이 빠르면 겹칩니다.
      if (currStart < prevEnd) {
        return false;
      }
    }

    // 겹치는 회의가 없으면 true를 반환합니다.
    return true;
  }
}
