// prefix sum 패턴을 사용한다.
// nums.length 길이의 정답 배열을 만들고 left, right 변수를 선언한다.
// 처음부터 for문으로 nums만 누적합 배열을 만들고 해결하려고 했던 게 실패 원인이었다. 변수 사용 및 계산식을 고려하지 못함.
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            output[i] = 1;
        }

        // 정답에 값을 적용하고 left, right을 업데이트한다는 점이 중요했다. -> 선적용 후업데이트를 잘못 이해해서 헤맸다.
        int left = 1;
        for (int i = 0; i < nums.length; i++) {
            output[i] *= left; // 1,2,2,6
            left *= nums[i]; // 1,2,6,24 (output 적용이 끝났으므로 24는 사실상 적용되지 않는다)
        }

        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            output[i] *= right; // 6,8,12,24 -> 배열 인덱스가 역순이기 때문에 결과적으로 [24, 12, 8, 6] 이 된다.
            right *= nums[i]; //
        }
        return output;
    }
}
