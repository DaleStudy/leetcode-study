import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/contains-duplicate/
 * TC : O(N)
 * SC : O(N)
 */
class Solution_0217 {

    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap();
        for (int n : nums) {
            if (map.containsKey(n)) {
                return true;
            } else {
                map.put(n, 1);
            }
        }
        return false;
    }
}
