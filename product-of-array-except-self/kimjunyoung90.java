public class kimjunyoung90 {
    public int[] productExceptSelf(int[] nums) {
        int[] answers = new int[nums.length];

        //왼쪽 값 계산
        answers[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            answers[i] = answers[i - 1] * nums[i - 1];
        }

        //오른쪽 값 계산
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answers[i] *= right;
            //다음 값 right 계산
            right *= nums[i];
        }
        return answers;
    }
}
