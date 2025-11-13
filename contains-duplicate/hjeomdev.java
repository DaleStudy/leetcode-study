import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set set = new HashSet();
        for (int num : nums) {
            set.add(num);
        }

        if (set.size() != nums.length) {
            return true;
        } else {
            return false;
        }
    }
}
