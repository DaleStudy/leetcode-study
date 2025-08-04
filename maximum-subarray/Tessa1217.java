/**
 정수 배열이 주어질 때 부분 수열의 가장 큰 합을 구하시오.
 */
class Solution {

    // 시간복잡도: O(n), 공간복잡도: O(1)
    public int maxSubArray(int[] nums) {

        int sum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            // 수 이어서 더할지 아니면 현재 값으로 초기화할지 여부 판단
            nums[i] = Math.max(nums[i], nums[i] + nums[i - 1]);
            sum = Math.max(nums[i], sum);
        }

        return sum;
    }

}

