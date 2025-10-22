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
import { MinHeap } from "@datastructures-js/heap";

export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: the minimum number of conference rooms required
   */
  // Time Complexity: O(n log n)
  // Space Complexity: O(n)
  minMeetingRooms(intervals: Interval[]): number {
    intervals.sort((a, b) => a.start - b.start);

    const minHeap = new MinHeap();
    const n = intervals.length;

    let maximumRooms = 0;
    for (let i = 0; i < n; i++) {
      const { start, end } = intervals[i];

      if (minHeap.isEmpty()) {
        minHeap.insert(end);
        maximumRooms = Math.max(maximumRooms, minHeap.size());
        continue;
      }

      if (start >= minHeap.root()) {
        minHeap.pop();
      }
      minHeap.insert(end);
      maximumRooms = Math.max(maximumRooms, minHeap.size());
    }
    return maximumRooms;
  }
}
