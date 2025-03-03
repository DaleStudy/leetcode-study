import {
  Interval,
} from '/opt/node/lib/lintcode/index.js';

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
    const sort = intervals.sort((a, b) => {
      if (a[1] === b[1]) {
          return a[0] - b[0];
      }

      return a[1] - b[1];
    })
    
    for (let i = 0; i < sort.length - 2; i++) {
      const current = sort[i][1];
      const next = sort[i + 1][0];

      if (current > next) {
          return false;
      }
    }

    return true;
  }
}

// 시간복잡도 O(nlogn) -> sort 함수 사용으로 인한 시간복잡도
// 공간복잡도 O(1) -> 사용하는 자료구조, 함수실행스택 없음
  
