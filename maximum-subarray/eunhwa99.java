
// 이전 솔루션과 동일
// 시간 복잡도: O(n) - n은 주어진 배열의 길이
// 공간 복잡도: O(1) - 상수 공간 사용
class Solution {

  public int maxSubArray(int[] nums) {
    int currentSum = nums[0];
    int maxSum = currentSum;
    for (int i = 1; i < nums.length; ++i) {
      currentSum = Math.max(currentSum + nums[i], nums[i]);
      maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
  }
}

