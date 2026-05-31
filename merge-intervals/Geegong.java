import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Geegong {

    /**
     * inerval 들을 오름차순으로 sorting 한후 각각의 start 와 end 를 비교하면서 머지할 수 경우를 고려하여 머지한다
     * time complexity : O(N) + O(N Long N) => O(N log N)
     * space complexity : O(N)
     * @param intervals
     * @return
     */
    public int[][] merge(int[][] intervals) {
        // 1. sort intervals
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));
        List<int[]> result = new ArrayList<>();

        result.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] last = result.get(result.size() - 1);
            int[] cur = intervals[i];

            if (last[1] >= cur[0]) {
                // merge (update last end)
                last[1] = Math.max(last[1], cur[1]);
            } else {
                // no overlap
                result.add(cur);
            }
        }

        return result.toArray(t -> new int[result.size()][]);
    }
}
