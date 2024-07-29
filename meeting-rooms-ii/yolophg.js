// Time Complexity: O(n log n)
// Space Complexity: O(n)

export class Solution {
  minMeetingRooms(intervals) {
    // separate start and end times into different arrays
    let startTimes = intervals.map((interval) => interval[0]);
    let endTimes = intervals.map((interval) => interval[1]);

    // sort the start and end times
    startTimes.sort((a, b) => a - b);
    endTimes.sort((a, b) => a - b);

    let startPointer = 0;
    let endPointer = 0;
    let rooms = 0;
    let maxRooms = 0;

    // iterate over all the start times
    while (startPointer < intervals.length) {
      // if the start time is less than the end time, a new room is needed
      if (startTimes[startPointer] < endTimes[endPointer]) {
        rooms++;
        startPointer++;
      } else {
        // if the start time is not less than the end time, free up a room
        rooms--;
        endPointer++;
      }

      // update the maximum number of rooms needed
      maxRooms = Math.max(maxRooms, rooms);
    }

    // return the maximum number of rooms needed
    return maxRooms;
  }
}
