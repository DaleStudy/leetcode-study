import java.util.ArrayList;
import java.util.List;

class Solution {

    // 시간, 공간복잡도: O(n)
    public int[][] insert(int[][] intervals, int[] newInterval) {

        // 병합된 interval 담는 list
        List<int[]> modifyIntervals = new ArrayList<>();

        int idx = 0;

        // 병합 이전 구간
        while (idx < intervals.length && intervals[idx][1] < newInterval[0]) {
            modifyIntervals.add(intervals[idx]);
            idx++;
        }

        // 병합이 필요한 구간 (newInterval과 겹치는 구간)
        while (idx < intervals.length && intervals[idx][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[idx][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[idx][1], newInterval[1]);
            idx++;
        }

        // 최종 병합된 새로운 interval add        
        modifyIntervals.add(newInterval);

        // 병합 이후 구간
        while (idx < intervals.length) {
            modifyIntervals.add(intervals[idx]);
            idx++;
        }

        return modifyIntervals.toArray(new int[modifyIntervals.size()][2]);
    }
}

