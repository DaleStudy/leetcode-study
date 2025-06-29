/**
 * 문제 설명
 * - 주어진 시간 간격에 대해 회의를 참석할 수 있는지 여부를 반환하는 문제
 *
 * 아이디어
 * 1) 시작 시간을 기준으로 정렬 후, 이전 회의의 종료 시간과 현재 회의의 시작 시간을 비교하여 참석 가능 여부를 판단
 *
 */

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
  /**
   * @param {Interval[]} intervals
   * @returns {boolean}
   */
  canAttendMeetings(intervals) {
    intervals = intervals.sort((a, b) => a.start - b.start);

    for (let i = 1; i < intervals.length; i++) {
      if (intervals[i].start < intervals[i - 1].end) {
        return false;
      }
    }
    return true;
  }
}
