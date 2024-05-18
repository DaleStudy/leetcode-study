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
    // Sort the intervals based on their start times
    intervals.sort((a, b) => a.start - b.start);

    for (let i = 0; i < intervals.length - 1; i++) {
      // Check if the current interval overlaps with the next interval
      if (intervals[i].end > intervals[i + 1].start) {
        return false;
      }
    }

    return true;
  }
}

// TC: O(nlogn)
// SC: O(1)
