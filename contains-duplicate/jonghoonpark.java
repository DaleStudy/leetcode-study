/*
 * https://leetcode.com/problems/contains-duplicate/
 * time complexity : O(n)
 * space complexity : O(n)
 * https://jonghoonpark.com/2024/04/24/leetcode-217
 */

/*
import java.util.HashSet;
import java.util.Set;

void main() {
    Solution solution = new Solution();
    System.out.println(solution.containsDuplicate(new int[]{1, 2, 3, 1})); // true
    System.out.println(solution.containsDuplicate(new int[]{1, 2, 3, 4})); // false
    System.out.println(solution.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})); // true
}

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            if (numSet.contains(num)) {
                return true;
            }
            numSet.add(num);
        }
        return false;
    }
}
*/