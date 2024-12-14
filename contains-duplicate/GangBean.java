import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        /***
            compare length of array and length of set.
            O(n) given that n is length of array nums
        */
        return nums.length > Arrays.stream(nums).boxed().collect(Collectors.toSet()).size();
    }
}
