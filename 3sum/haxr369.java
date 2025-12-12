import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 세 수의 인덱스가 모두 다르고 세 수 합이 0인 경우의 수를 구하기
 * 세 숫자가 들어간 배열은 중복되게 하지 않은다.
 * 
 * 1. 모든 경우의 수를 구한다. => O(N^3)
 * 3000*3000*3000 == 9*10^9 => 9억건...
 * 2. left, mid, right라고 할 때, mid를 고정하고 left, right만 움직이는 two pointer를 응용하기
 */
class Solution {
  /**
   * Runtime: 545 ms (Beats 14.44%)
   * Memory: 60.78 MB (Beats 5.38%)
   * Space Complexity: O(N)
   * - 정렬을 위한 공간 => O(N)
   * - 세 수를 저장하기 위한 리스트 => O(3)
   * > O(N) + O(3) => O(N)
   * Time Complexity: O(NlogN)
   * - 정렬을 위한 시간 => O(NlogN)
   * - mid의 순회 => O(N)
   * - two pointer 조회 => O(N)
   * > O(NlogN) + O(N)*O(N) ~= O(N^2)
   */
  public List<List<Integer>> threeSum(int[] nums) {
    int L = nums.length;
    Arrays.sort(nums);

    Set<List<Integer>> st = new HashSet<>();

    // mid를 늘려가면서 투 포인터 진행
    for (int mid = 1; mid < L - 1; mid++) {
      int left = 0;
      int right = L - 1;
      while (left < mid && mid < right) {
        int sm = nums[left] + nums[mid] + nums[right];
        if (sm == 0) {
          /**
           * left를 더하는 이유:
           * 현재 찾은 경우의 수 외에 다른 경우가 존재할 수 있음
           * ex) -7,1,6 / -6,1,5
           * => mid는 고정이지만, left는 늘리고 right를 줄여서 0을 만들 수 있는 다른 경우가 있음
           */
          List<Integer> li = new ArrayList<>();
          li.add(nums[left]);
          li.add(nums[mid]);
          li.add(nums[right]);
          st.add(li); // 중복값이 있어도 무시할 수 있음.
          left++;
        } else if (sm < 0) { // 부족하면 left 늘리기
          left++;
        } else { // 과하면 right 줄이기
          right--;
        }
      }
    }

    return new ArrayList<>(st);
  }
}
