class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] front = new int[nums.length];
        int[] back = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            front[i] = 1;
            back[i] = 1;
        }

        for (int i = 0; i < nums.length - 1; i++) {
            front[i + 1] = front[i] * nums[i];
        }

        for (int i = nums.length - 1; i > 0; i--) {
            back[i - 1] = nums[i] * back[i];
        }

        for (int i = 0; i < nums.length; i++) {
            answer[i] = front[i] * back[i];
        }

        return answer;
    }
}
