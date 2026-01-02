import java.util.HashSet;

// link: https://leetcode.com/problems/contains-duplicate/description/
// difficulty: Easy
class Solution {
    // Problem:
    // * return: does any value appear more than once in the array
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity: O(N)
    public boolean containsDuplicate(int[] nums) {
        // Space Complexity: O(N)
        HashSet<Integer> uniqNums = new HashSet<>();

        // Time Complexity: O(N)
        for(int num : nums) {
            if(!uniqNums.add(num)) return true;
        }

        return false;
    }
}
