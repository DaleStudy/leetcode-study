class Solution {
    public int[][] merge(int[][] intervals) {

        if (intervals.length <= 1) {
            return intervals;
        }

        List<int[]> answer = new ArrayList<>();

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {

            // 현재 인터벌 시작점
            int currStart = intervals[i][0];
            // 현재 인터벌 끝점 
            int currEnd = intervals[i][1];

            if (end >= currStart) {
                end = Math.max(end, currEnd);                
            } else {
                answer.add(new int[]{start, end});
                start = currStart;      
                end = currEnd;
            }            
        }

        answer.add(new int[]{start, end});

        return answer.stream()
                            .toArray(int[][]::new);
    }
}

