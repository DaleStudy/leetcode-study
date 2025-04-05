import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        /**
         avg : O(NlogN)
         worst : O(N^2)
         */
        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] == nums[i]) return true;
        }

        return false;
    }
}
