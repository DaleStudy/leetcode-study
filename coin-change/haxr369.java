import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

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

    return ans;
  }

}