/**
	탐욕법을 이용하여, 연산하는 방식
*/
class Solution {
    public int[][] merge(int[][] intervals) {
        
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        
        List<int[]> result = new ArrayList<>();
        int startNum = intervals[0][0];
        int endNum = intervals[0][1];
        for(int i = 1; i < intervals.length; i++) {
            if(endNum >= intervals[i][0]) {
                endNum = Math.max(endNum, intervals[i][1]);
                continue;
            }
                
            result.add(new int[]{startNum, endNum});
            startNum = intervals[i][0];
            endNum = intervals[i][1];
        }
        result.add(new int[]{startNum, endNum});
        
        return result.toArray(new int[result.size()][]);
    }
}
