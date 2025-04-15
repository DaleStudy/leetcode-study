// 시간 복잡도: O(n) - nums 배열의 길이 n
// 공간 복잡도: O(n) - leftProduct와 rightProduct 배열을 사용
class Solution {

  public int[] productExceptSelf(int[] nums) {
    int[] leftProduct = new int[nums.length];
    int[] rightProduct = new int[nums.length];

    for (int i = 0; i < nums.length; i++) {
      if (i == 0) {
        leftProduct[i] = 1;
      } else {
        leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
      }
    }

    for (int i = nums.length - 1; i >= 0; i--) {
      if (i == nums.length - 1) {
        rightProduct[i] = 1;
      } else {
        rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
      }
    }

    int[] result = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
      result[i] = leftProduct[i] * rightProduct[i];
    }
    return result;
  }
}


