/**
 <a href="https://leetcode.com/problems/contains-duplicate/">week01-1.contains-duplicate</a>
 <li> Description: return true if any value appears at least twice in the array  </li>
 <li> Concept: Array, Hash Table, Sorting    </li>
 <li> Time Complexity: O(n), Runtime: 11ms   </li>
 <li> Space Complexity: O(n), Memory: 59.27MB </li>
 */

class Solution {
    Set<Integer> set = new HashSet<>();

    public boolean containsDuplicate(int[] nums) {
        return !Arrays.stream(nums).allMatch(set::add);
    }
}
