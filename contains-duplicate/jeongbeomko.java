import java.util.HashSet;

/*
* 시간복잡도: O(n)
* 공간복잡도: O(n)
* */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> numSet  = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {

            if (numSet.contains(nums[i])) {
                return true;
            }
            numSet.add(nums[i]);
        }

        return false;
    }
}
