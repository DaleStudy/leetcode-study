import java.util.HashSet;
import java.util.Set;

class Solution {

    public boolean containsDuplicate(int[] nums) {

        Set<Integer> distincts = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            distincts.add(nums[i]);
        }

        return distincts.size() != nums.length;
    }
}
