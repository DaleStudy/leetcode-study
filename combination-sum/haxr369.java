import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 1번째 풀이는 2번째 풀이를 개선한 것.
 * 2번째 풀이는 dfs를 이욯해서 중복순열의 경우의 수를 찾기 때문에 시간복잡도가 매우 높다.
 * 또한 중복순열에서 중복을 제거하면서도 낭비되는 연산이 매우 많다.
 * 
 */
class Solution {

  /**
   * candidates의 후보들은 중복 사용이 가능하다.
   * 모든 후보는 구별된다.=> 중복이 없다.
   * 
   * Runtime: 48 ms (Beats 5.56%)
   * Memory: 46.96 MB (Beats 6.1%)
   * Space Complexity: O(N) + O(K)
   * - 사용되는 후보를 Set으로 관리하기 => O(N)
   * - 후보가 사용된 횟수를 관리하기 => O(K)
   * > O(N) + O(K)
   * Time Complexity: O(N)
   * - 후보 하나를 선택해서 target과 비교 => O(N^M)
   * - target이 0이 되거나 누적 값이 더 커질 때까지 스택을 쌓기
   * - 최대 누적할 수 있는 횟수는 40 / 2 = 20회 => O(20) = O(M)
   * > O(N)*O(M)
   */
  public List<List<Integer>> combinationSum2(int[] candidates, int target) {
    Set<List<Integer>> set = new HashSet<>();
    Set<Integer> acc = new HashSet<>();
    int[] usedCount = new int[44];
    dfs(set, acc, usedCount, target, candidates);

    List<List<Integer>> ans = new ArrayList<>(set);
    return ans;
  }

  /**
   * set: return용 조합 저장
   * acc: 사용 후보 누적
   * usedCount: 후보별 사용된 횟수 저장
   * target: 만들 수
   */
  private void dfs(Set<List<Integer>> set, Set<Integer> acc, int[] usedCount, int target, int[] candidates) {
    // 완성된 경우 리턴하기
    if (target == 0) {
      // System.out.println("==========완성!! -> "+acc);
      List<Integer> tmp = new ArrayList<>();
      for (int n : candidates) {
        if (acc.contains(n)) {
          for (int i = 0; i < usedCount[n]; i++) {
            tmp.add(n);
          }
        }
      }
      set.add(tmp);
      return;
    }

    for (int n : candidates) {
      // target 보다 작은 후보 사용하기

      if (target >= n) {
        // System.out.println("candi->"+n);
        usedCount[n]++;
        acc.add(n);
        // System.out.println(". next target->"+(target-n));
        dfs(set, acc, usedCount, target - n, candidates);
        // 원복하기
        usedCount[n]--;
        if (usedCount[n] == 0) {
          acc.remove(n);
        }
      }
    }
  }
}