/**
 * 시간 복잡도: 정렬의 시간 복잡도와 같음. O(nlogn)
 * 공간 복잡도: 자바스크립트의 정렬은 Timsort를 사용. 따라서 최악의 경우 공간 복잡도는 O(n)
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
      intervals.sort((a,b) => a.start - b.start)

      for(let i = 1; i < intervals.length; i++) {
          if(intervals[i].start < intervals[i-1].end) {
              return false;
          }
      }
      return true;
  }
}
