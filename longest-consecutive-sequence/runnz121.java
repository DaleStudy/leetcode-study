import java.util.*;
import java.util.stream.Collectors;

public class runnz121 {

    public class Solution {

        public int longestConsecutive(int[] nums) {

            if (nums.length == 0) {
                return 0;
            }

            Set<Integer> collect = Arrays.stream(nums).boxed().collect(Collectors.toSet());
            int[] array = collect.stream().mapToInt(Integer::intValue).toArray();

            List<Integer> minus = new ArrayList<>();
            List<Integer> plus = new ArrayList<>();

            for (int i = 0; i < collect.size(); i++) {

                if (array[i] < 0) {
                    minus.add(array[i]);
                } else {
                    plus.add(array[i]);
                }
            }

            Collections.sort(minus);
            Collections.sort(plus);

            List<Integer> total = new ArrayList<>();
            total.addAll(minus);
            total.addAll(plus);

            int ans = 0;
            int subAns = 1;
            for (int i = 0; i < total.size() - 1; i++) {
                if (total.get(i + 1) == total.get(i) + 1) {
                    subAns += 1;
                } else {
                    ans = Math.max(subAns, ans);
                    subAns = 1;
                }
            }

            ans = Math.max(ans, subAns);

            return ans;
        }
    }
}
