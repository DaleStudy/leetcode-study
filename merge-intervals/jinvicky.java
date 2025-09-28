import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[][] merge(int[][] intervals) {
        // 1. [0]번째 위주로 오름차순 정렬한다. 
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        // [0], [1] 을 start, end로 선언한다. 
        int start = intervals[0][0];
        int end = intervals[0][1];

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < intervals.length; i++) {
            int curS = intervals[i][0];
            int curE = intervals[i][1];

            if(curS <= end) {
                end = Math.max(curE, end);
            } else {
                start = curS;
                end = curE;
            }

            // {1,3} , {1,6}이 차례로 들어왔을 때 더 나중에 들어온 값으로 overlapp 될 것이라는 점을 이용했다. 
            map.put(start, end);
        }

        int[][] answer = new int[map.size()][2];

        int idx = 0;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int[] item = new int[]{entry.getKey(), entry.getValue()};
            answer[idx] = item;
            idx++;
        }

        return answer;
    }
}
