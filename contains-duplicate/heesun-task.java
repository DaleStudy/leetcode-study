class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Create a set to track seen numbers
        Set<Integer> seen = new HashSet<>();

        // Loop through the array and return true if a duplicate is found
        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }

        return false;
    }
}

// Time Complexity: O(n) on average
// Space Complexity: O(n)
