class Solution {
    public int[][] merge(int[][] intervals) {
        /**
        1.prob: overlapping 되는 곳을 merge 해서 return
        2.constraints
        - len(intervalse) min = 1, max= 10000
        - start, end value min = 0, max = 10000
        3.solution
        - sorting array -> merge overlapping values
        time: O(n log n)
         */

       int n = intervals.length;
       Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

       List<int[]> answer = new ArrayList<>();
       int start = intervals[0][0];
       int end = intervals[0][1];

       for(int i = 1; i < n; i++) {
        int nextStart = intervals[i][0];
        int nextEnd = intervals[i][1];

        //overlap
        if(end >= nextStart) {
            end = Math.max(end, nextEnd);
        } else {
            answer.add(new int[]{start, end});

            start = nextStart;
            end = nextEnd;

        }
       }

        //last intervals
        answer.add(new int[]{start, end});
        return answer.toArray(new int[answer.size()][]);
    }
}
