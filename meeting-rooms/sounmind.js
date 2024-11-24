/**
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
    intervals.sort((a, b) => a[0] - b[0]);

    for (let i = 1; i < intervals.length; i++) {
      const startTime = intervals[i][0];
      const previousMeetingEndTime = intervals[i - 1][1];

      if (previousMeetingEndTime > startTime) {
        return false;
      }
    }

    return true;
  }
}

/**
 * Time complexity: O(nlogn), where n is the number of meetings
 * Reason:
 *  We sort the meetings by start time, which takes O(nlogn) time.
 *  Then we iterate through the meetings once, which takes O(n) time.
 *
 * Space complexity: O(1)
 * Reason: We use a constant amount of extra space.
 */
