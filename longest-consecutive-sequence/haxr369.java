import java.util.Arrays;

class Solution {
  /**
   * 13분 소요.
   * Runtime: 23 ms (Beats 80.31%)
   * Memory: 77.33 (Beats 9.66%)
   * Space Complexity: O(N)
   * - 원소 배열 정렬은 듀얼 피봇 sort => O(logN)
   * > O(N) + O(logN) ~= O(N)
   * Time Complexity: O(NlogN)
   * - 듀얼 피봇 sort를 이용한 정렬 => O(NlogN)
   * - 배열을 처음부터 끝까지 조회, 이전 값과 비교 => O(N)*O(1)
   * > O(NlogN) + O(N) ~= O(NlogN)
   */
  public int longestConsecutive(int[] nums) {
    Arrays.sort(nums);

    if (nums.length == 0) {
      return 0;
    }
    int ans = 1;
    int seqLgth = 1;
    for (int i = 1; i < nums.length; i++) {
      // 바로 연결되는 경우는 바로 이전 요소 보다 1이 더 커야함.
      if (nums[i - 1] < nums[i] && nums[i] - nums[i - 1] == 1) {
        nums[i - 1] = nums[i];
        seqLgth++;
        ans = Integer.max(ans, seqLgth); // 항상 ans 업데이트 하기
      } else if (nums[i - 1] < nums[i] && nums[i] - nums[i - 1] > 1) {
        // 새로운 연결로 들어가기
        seqLgth = 1;
      }
    }
    return ans;
  }
}