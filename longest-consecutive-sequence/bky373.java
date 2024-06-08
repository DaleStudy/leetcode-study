/**
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int n : nums) {
            numSet.add(n);
        }
        int longest = 0;
        for (int n : nums) {
            if (numSet.contains(n - 1)) {
                continue;
            }
            int seq = 1;
            while (numSet.contains(n + seq)) {
                seq++;
            }
            longest = Math.max(longest, seq);
        }
        return longest;
    }
}
