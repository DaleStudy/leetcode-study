class Solution {
  /**
   * @param {Interval[]} intervals
   * @returns {number}
   */
  minMeetingRooms(intervals) {
    // Edge case
    if (intervals.length === 0) return 0;

    let startTimes = intervals.map((interval) => interval.start);
    let endTimes = intervals.map((interval) => interval.end);

    startTimes.sort((a, b) => a - b);
    endTimes.sort((a, b) => a - b);

    let roomNeeded = 0;
    let endIndex = 0;

    for (let i = 0; i < intervals.length; i++) {
      if (startTimes[i] < endTimes[endIndex]) roomNeeded++;
      else endIndex++;
    }

    return roomNeeded;
  }
}

// TC: O(nlogn)
// SC: O(n)
