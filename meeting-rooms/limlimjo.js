// 시간복잡도: O(nlogn)
// 공간복잡도: O(1)

export class Solution {

    canAttendMeetings(intervals) {
      // Write your code here
      intervals.sort((a, b) => a[0] - b[0]);
        
      for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < intervals[i - 1][1]) {
            return false;
        }
      }
        return true;
    }
  }

