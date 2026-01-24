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
        int[] prev = intervals[0];
        for (int idx = 1; idx<intervals.length; idx++) {

            int[] current = intervals[idx];

            // 2. merge
            if (prev[1] >= current[0]) {
                // if there is value in temp merge , currently merged
                int[] last = result.get(result.size() - 1);
                int[] newThing = new int[]{last[0], Math.max(last[1], current[1])} ;
                result.remove(result.size() - 1);
                result.add(result.size() - 1, newThing);

            } else {

                // 3. no merge
                result.add(new int[]{current[0], current[1]});
            }

            prev = current;
        }

        return result.toArray(t -> new int[result.size()][]);
    }
}
