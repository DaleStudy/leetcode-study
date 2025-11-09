import java.util.HashSet;
import java.util.Set;

class SolutionLongestConsecutiveSequence {

  public int longestConsecutive(int[] nums) {
      // 시퀀스 조회를 O(1)에 수행 가능하고, 중복은 무시할 수 있는 조건이므로 Set이 적합한 자료구조
      // 시간복잡도: O(N), 공간복잡도: O(N)
      Set<Integer> num_set = new HashSet<Integer>();
      for (int num : nums) {
          num_set.add(num);
      }

      int longestSequence = 0;

      // 시간복잡도: O(N)
      for (int num : num_set) {
          // 시퀀스 중간에 있는 숫자가 아닌 시작하는 숫자를 찾음
          // 시작하는 숫자는 - 1 값이 Set에 없을 것
          if (!num_set.contains(num - 1)) {
              int currentNum = num;
              int currentLength = 1;
              // + 1 값이 Set에 있는 지 확인하면서 증가
              while (num_set.contains(currentNum + 1)) {
                  currentNum += 1;
                  currentLength += 1;
              }

              // 순회가 끝나면 최대 시퀀스 길이인지 확인하고 적용
              longestSequence = Math.max(longestSequence, currentLength);
          }
      }

      return longestSequence;
  }
}
