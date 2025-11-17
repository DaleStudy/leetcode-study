import { Interval } from "../home/lib/index";
/**
 * Definition of Interval:
 * export class Interval {
 *     start :number;
 *     end :number;
 *     constructor(start :number, end :number) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

export class Solution {
  /**
   * Time Complexity: O(nlogn)
   * Space Complexity: O(1)
   *
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals: Interval[]): boolean {
    if (intervals.length <= 1) return true;

    intervals.sort((a, b) => a.start - b.start);

    let prevEnd = intervals[0].end;
    for (let i = 1; i < intervals.length; i++) {
      const currentStart = intervals[i].start;
      const currentEnd = intervals[i].end;

      if (prevEnd > currentStart) {
        return false;
      }
      prevEnd = currentEnd;
    }

    return true;
  }
}
