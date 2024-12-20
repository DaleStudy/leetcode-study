import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        if(numSet.size()!=nums.length) return true;
        else return false;
    }
}
