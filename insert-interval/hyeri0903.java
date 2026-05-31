class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        /**
        1.문제: newInterval 을 추가 후 intervals 오름차순 재정렬
        2.constraints: start 기준으로 ascending order
        3.solutions
        - newIntervals start 보다 앞에있는 것들은 merge 필요 없음
        - 즉 intervalse[i][1] < newInterval[0] 이면 merge X
        - intervals[i][0] <= newInterval[1] 이면 merge
        - 마지막에 겹치는 부분은 skip 후 intervals 재정렬
        time: O(n), space: O(1)
         */

         List<int []> result = new ArrayList<>();
         int i = 0;
         int n = intervals.length;

         //1.newInterval 앞에 있는 값은 그대로 result add
         while(i < n && intervals[i][1] < newInterval[0]) {
            result.add(intervals[i]);
            i += 1;
         }

         //2.overlap 구간은 merge
         while(i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i += 1;
         }
         result.add(newInterval);

         //3.나머지 result에 add
         while(i < n) {
            result.add(intervals[i]);
            i++;
         }

         return result.toArray(new int[result.size()][]);
        
    }
}
