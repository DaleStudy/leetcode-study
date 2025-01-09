// subarray = "연속된 값"의 합을 요구 함 그래서 간단한 풀이가 가능하다.
// 이전 인덱스나 값들을 기억할 필요가 없어서 누적합 느낌으로 풀 수 있다.
// 키포인트는 이전까지의 합보다 다음 숫자가 큰 경우의 수가 존재한다는 것
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int current = nums[0];

        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            max = Math.max(max, current);
        }

        return max;
    }
}
