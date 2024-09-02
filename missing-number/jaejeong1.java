class SolutionMissingNumber {
  public int missingNumber(int[] nums) {
    // N = 배열의 길이
    // 0 ~ N 의 합을 구하고, nums의 모든 값을 다 빼면 정답
    // 시간복잡도: O(N), 공간복잡도: O(1)
    var N = nums.length;
    var sum = (N * (N+1)) / 2;

    for (var num : nums) {
      sum -= num;
    }

    return sum;
  }
}
