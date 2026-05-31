import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
  /**
   * 30분 38초 소요.
   * nums에서 가장 자주 등장하는 k개 숫자 리턴하기
   * Map에 요소:등장수로 관리하기
   * Stream으로 등장수 기준으로 내림차순 정렬 후 k개만 리스트로 만들어서 출력한다.
   * 
   * Java의 Stream과 Comparator 사용법을 익혀야함.
   * Comparable도 몰랐던 부분.
   */
  public int[] topKFrequent(int[] nums, int k) {
    /**
     * Runtime: 21 ms (Beats 6.30%)
     * Memory: 47.42 (Beats 83.73%)
     * Space Complexity: O(N)
     * - HashMap 공간복잡도 => O(N)
     * - sort에서 tim sort 사용 => O(N)
     * > O(N)
     * Time Complexity: O(NlogN)
     * - tim sort를 이용한 정렬 => O(NlogN)
     * > O(N) + O(NlogN) + O(N) ~= O(NlogN)
     */

    Map<Integer, Integer> mp = new HashMap<>();
    for (int n : nums) {
      if (mp.containsKey(n)) {
        mp.put(n, mp.get(n) + 1);
      } else {
        mp.put(n, 1);
      }
    }
    List<Integer> li = mp.entrySet().stream()
        // 값을 기준으로 내림차순 정렬
        .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
        .limit(k)
        .map(Map.Entry::getKey)
        .collect(Collectors.toList());

    int[] ans = new int[li.size()];
    for (int i = 0; i < li.size(); i++) {
      ans[i] = li.get(i);
    }
    return ans;
  }
}
