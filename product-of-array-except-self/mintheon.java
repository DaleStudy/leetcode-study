class Solution {
  /**
   공간복잡도: O(n)
   시간복잡도: O(n)
   */
  public int[] productExceptSelf(int[] nums) {
    int[] answer = new int[nums.length];

    answer[0] = 1;
    for(int i = 1; i < nums.length; i++) {
      answer[i] = answer[i - 1] * nums[i - 1];
    }

    int value = 1;
    for(int i = nums.length - 1; i >= 0; i--) {

      answer[i] = answer[i] * value;
      value *= nums[i];
    }

    return answer;
  }
}
