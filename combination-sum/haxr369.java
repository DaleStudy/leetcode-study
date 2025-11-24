import java.util.ArrayList;
import java.util.Arrays;
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
   * 중복순열을 구하는 부분은 2번 풀이와 동일하지만,
   * 후보배열을 정렬하고, 후보 선택 시 이전 값과 같거나 큰 후보만을 선택하기에
   * 동일 요소가 존재하는 배열을 중복해서 만들지 않음.
   * 또한 Set 같은 저장위치를 제거해서 메모리 최적화.
   * 
   * Runtime: 5 ms (Beats 8.49%)
   * Memory: 45.77 MB (Beats 16.78%)
   * Space Complexity: O(N)
   * - 사용된 후보를 저장하는 배열 O(N)
   * > O(N)
   * Time Complexity: O(2^N/N!)
   * - 후보 하나를 선택해서 target과 비교 => O(2^N)
   * - target이 0이 되거나 누적 값이 더 커질 때까지 스택을 쌓기
   * - 최대 누적할 수 있는 횟수는 40 / 2 = 20회 => O(20) = O(M)
   * - 다만, 중복배열 생성을 방지하는 트릭을 추가함 O(1/N!)
   * > O(2^N/N!)
   * 
   * @param candidates
   * @param target
   * @return
   */
  public List<List<Integer>> combinationSum(int[] candidates, int target) {
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> acc = new ArrayList<>();
    Arrays.sort(candidates);

    makecombination(ans, acc, target, candidates, 0);
    return ans;
  }

  /**
   * 이전에 더했던 후보와 같거나 큰 후보만 더한다.
   * set: return용 조합 저장
   * acc: 사용 후보 누적
   * usedCount: 후보별 사용된 횟수 저장
   * target: 만들 수
   */
  private void makecombination(List<List<Integer>> set, List<Integer> acc, int target, int[] candidates,
      int idx) {
    // 완성된 경우 리턴하기
    if (target == 0) {
      List<Integer> tmp = new ArrayList<>(acc); // 깊은 복사
      set.add(tmp);
      return;
    } else if (target < 0 || idx >= candidates.length) { // 타겟이 0 보다 작은 경우 스킵
      return;
    }

    // 현재 인덱스 후보 사용
    acc.add(candidates[idx]);
    makecombination(set, acc, target - candidates[idx], candidates, idx);
    acc.remove(acc.size() - 1); // 마지막 요소 제거

    // 다음 인덱스 후보 사용
    makecombination(set, acc, target, candidates, idx + 1);
    return;
  }

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
   * Time Complexity: O(2^N)
   * - 후보 하나를 선택해서 target과 비교
   * - target이 0이 되거나 누적 값이 더 커질 때까지 스택을 쌓기 => O(2^N)
   * > O(2^N)
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
   * target을 만드는 순열을 만든다.. => 중복을 포함하기 때문에 중복 연산이 많다..
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