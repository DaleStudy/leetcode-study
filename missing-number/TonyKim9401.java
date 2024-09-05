// TC: O(n)
// -> add all nums into set
// SC: O(n)
// -> set contains all nums' elements
class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int output = 0;
        while (set.contains(output)) output += 1;

        return output;
    }
}
