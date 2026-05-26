class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        /**
        1.prob: 겹치지 않는 최소한의 non-oerlapping interval 제거
        2.constraints
        - inverval.lenght min=1, max = 100,000
        3.solutions - Greedy
        - end 기준 오름차순 정렬
        - 이전 interval end 저장
        - 다음 interval check, 안겹치면 -> 선택, 겹치면 count++
        Time: O(n logn), Space: O(1)
         */
         int count = 0;
    
         //end 기준 ascending 정렬
         Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
          int end = intervals[0][1];

         //겹치면 count++, 안겹치면 end update
         for(int i = 1; i < intervals.length; i++) {
                if(intervals[i][0] < end) {
                    count++;
                } else {
                    end = intervals[i][1];
                }
         }

        return count;
    }
}
