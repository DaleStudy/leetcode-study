class SolutionProductExceptSelf {

  public int[] productExceptSelf(int[] nums) {
    // answer[i] = nums[0] * nums[1] * ... * nums[i-1] * nums[i+1] * ... * nums[n-1]
    // answer[i] = left[i] * right[i]
    // left[i] = nums[0] * nums[1] * ... * nums[i-1]
    // right[i] = nums[i+1] * ... * nums[n-1]
    // left[i] = left[i-1] * nums[i-1]
    // right[i] = right[i+1] * nums[i+1]
    // answer[i] = left[i] * right[i]
    // 시간복잡도: O(N), 공간복잡도: O(N)
    int n = nums.length;
    int[] left = new int[n];
    int[] right = new int[n];
    int[] answer = new int[n];

    left[0] = 1;
    right[n - 1] = 1;

    for (int i = 1; i < n; i++) {
      left[i] = left[i - 1] * nums[i - 1];
    }

    for (int i = n - 2; i >= 0; i--) {
      right[i] = right[i + 1] * nums[i + 1];
    }

    for (int i = 0; i < n; i++) {
      answer[i] = left[i] * right[i];
    }

    return answer;
  }
}