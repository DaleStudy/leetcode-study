import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * 79/79 cases passed (19 ms)
     * Your runtime beats 32.04 % of java submissions
     * Your memory usage beats 6.16 % of java submissions (108.1 MB)
     *
     * When I changed HashSet to LinkedHashSet, the runtime and memory usage increased a little bit.
     *
     * Improvement:
     * if (!set.add(num)) return true;  // when num is already in the set, return true.
     * It looks like more simple.
     */
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> exist = new HashSet<>();

        for (int num : nums) {
            if (exist.contains(num)) {
                return true;
            } else {
                exist.add(num);
            }
        }
        return false;
    }
}
