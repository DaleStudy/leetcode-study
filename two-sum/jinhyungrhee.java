class Solution {

    // Method1. brute-force => O(N^2)
    public int[] twoSum(int[] nums, int target) {
        int size = nums.length;
        int[] answer = new int[2];
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (nums[i] + nums[j] == target) {
                    answer[0] = i;
                    answer[1] = j;
                }
            }
        }
        return answer;
    }
}
