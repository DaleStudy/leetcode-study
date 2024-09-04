// TC: O(n)
// SC: O(n)
class Solution {
    public int longestConsecutive(int[] nums) {
        int output = 0;
        Set<Integer> set = new HashSet<>();

        for (int num : nums) set.add(num);

        for (int num : nums) {
            int count = 1;
            if (!set.contains(num - count)){
                while (set.contains(num + count)) {
                    count += 1;
                }
            }
            output = Math.max(output, count);
        }
        return output;
    }
}
