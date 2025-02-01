class Solution {

  // TP: O(N)
  // SP: O(1)
  // 음수 원소를 처리하기 위해 곱의 Min 값도 생각해야 했던 문제!
  public int maxProduct(int[] nums) {

    int minProd = nums[0];
    int maxProd = nums[0];
    int result = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < 0) {
        int temp = minProd;
        minProd = maxProd;
        maxProd = temp;
      }

      maxProd = Math.max(nums[i], maxProd * nums[i]);
      minProd = Math.min(nums[i], minProd * nums[i]);
      result = Math.max(result, maxProd);
    }

    return result;
  }
}

