/*
Runtime: 10 ms(Beats: 89.16 %)
Time Complexity: O(n)
- HashSet r/w : O(1)
- nums iteration : ( O(1) + O(1) ) * n = O(n)

Memory: 58.63 MB(Beats: 22.32 %)
Space Complexity: O(n)
*/


class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            if (set.contains(num)) {
                return true;
            }

            set.add(num);
        }

        return false;
    }
}
