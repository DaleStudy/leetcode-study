import java.util.Arrays;

class Solution {
  /**
   * 합해서 target이 되는 두 수의 인덱스를 배열에 넣어서 return.
   * 1. nums 정렬하기
   * 2. smlNumbIdx(초기 0), lrgNumbIdx(초기 nums.length - 1)에 인덱스를 저장
   * 3. smlNumb와 lrgNumb를 합해서 tmp를 계산
   * 4. tmp와 target을 비교.
   * 4.1. tmp < target인 경우
   * smlNumbIdx에 1 더하기
   * 4.2. tmp > target인 경우
   * lrgNumbIdx에 1 빼기
   * 4.3. tmp = target인 경우
   * smlNumbIdx와 lrgNumbIdx 배열 return
   */
  public int[] twoSum(int[] nums, int target) {
    /**
     * Runtime: 8 ms (Beats 47.90%)
     * Memory: 46.70 (Beats 5.05%)
     * Space Complexity: O(N)
     * > Arrays.sort의 객체 타입은 tim sort를 이용하기 때문에 O(N)을 가짐
     * Time Complexity: O(NlogN)
     * - 크기 Nx2 배열에 값과 인덱스를 넣기 => O(N)
     * - tim sort를 이용한 정렬 => O(NlogN)
     * - N회 for문으로 정답 인덱스 찾기 => O(N)
     * > O(N) + O(NlogN) + O(N) ~= O(NlogN)
     */
    int[][] arr = new int[nums.length][2];
    for (int i = 0; i < nums.length; i++) {
      arr[i][0] = nums[i];
      arr[i][1] = i;
    }
    Arrays.sort(arr, (a, b) -> {
      if (a[0] != b[0])
        return Integer.compare(a[0], b[0]);
      return 1; // 동일하면 상관 없음.
    });

    int smlNumbIdx = 0;
    int lrgNumbIdx = nums.length - 1;
    for (int i = 0; i < arr.length; i++) {
      if (arr[smlNumbIdx][0] + arr[lrgNumbIdx][0] == target) {
        int[] ans = { arr[smlNumbIdx][1], arr[lrgNumbIdx][1] };
        return ans;
      } else if (arr[smlNumbIdx][0] + arr[lrgNumbIdx][0] < target) {
        smlNumbIdx++;
      } else {
        lrgNumbIdx--;
      }
    }

    // 문제는 없지만, 예외케이스가 발생할 수 있으니 더미 데이터 출력
    int[] ans = { 0, nums.length };
    return ans;
  }
}
