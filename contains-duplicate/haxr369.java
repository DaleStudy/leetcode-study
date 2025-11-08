class Solution {
  public boolean containsDuplicate(int[] nums) {
    /**
     * Runtime: 14 ms (Beats 62.49%)
     * Space Complexity: O(N)
     * > nums 배열 길이 N. 중복하지 않은 모든 요소가 Set에 들어가기 때문에 O(N)
     * Time Complexity: O(N) ~ O(NlogN)
     * - 크기 N 배열 조회에 O(N)
     * - Set에 숫자 중복 체크 O(1)
     * - 단, 최악에 경우로 중복 체크에 O(logN)이 발생 가능
     * > O(N) * O(1) ~ O(NlogN)
     * Memory: 93.28 (Beats 6.24%)
     */
    Set<Integer> st = new HashSet<>();
    for (int n : nums) {
      if (st.contains(n)) {
        return true;
      }
      st.add(n);
    }
    return false;

  }
}