import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();

        for (int n : nums) {
            set.add(n);
        }

        for (int n : set) {
            if (set.contains(n - 1)) continue;

            int cur = n;
            int count = 1;

            while (set.contains(cur + 1)) {
                cur += 1;
                count += 1;
            }

            answer = Math.max(answer, count);
        }

        return answer;
    }
}
