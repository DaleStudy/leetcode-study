import java.util.HashSet;

class Solution {
    // return: does any value appear more than once in the array
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniqNums = new HashSet<>();

        for(int num : nums) {
            if(!uniqNums.add(num)) return true;
        }

        return false;
    }
}
