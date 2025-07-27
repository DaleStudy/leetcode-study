class Solution {
    public int[] productExceptSelf(int[] nums) {

        // 원래는 그냥 다 곱해서 자기 빼고 나누면 되는데 나눗셈 하지 말라고 함

        // 왼쪽 곱 구한다음에 오른쪽 곱으로 리턴하면 됨
        int[] answer = new int[nums.length];

        int left = 1;
        answer[0] = left;

        for (int i = 1; i < nums.length; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // 1 1 2 6

        // 오른쪽 누적 곱

        int right = 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] = answer[i] * right;
            right *= nums[i];
        }


        return answer;

    }
}