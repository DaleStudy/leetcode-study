import java.util.HashSet;
import java.util.Set;


class Solution {

    /**
     *
     * Set 판단으로 O(n)
     *
     * */
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> set = new HashSet<>();

        for (int num : nums) {

            boolean isAdded = set.add(num);

            if (!isAdded) {
                return true;
            }
        }

        return false;

    }
}
