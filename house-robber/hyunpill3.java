class Solution {
    public int rob(int[] nums) {
        int next = 0;
        int next2 = 0;

        for (int num : nums) {
            int current = Math.max(next, next2 + num);

            next2 = next;
            next = current;
        }

        return next;
    }
}