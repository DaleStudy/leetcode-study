import java.util.HashSet;
import java.util.Set;

class SolutionLongestConsecutiveSequence {

  public int longestConsecutive(int[] nums) {
    // 정렬되지 않은 정수 nums 배열이 주어지면 가장 긴 연속 요소 시퀀스 길이를 반환
    // O(N) 시간 내 실행되야함
    // 전부 해시맵에 때려넣고, 키를 꺼내 연속 요소가 있는지 확인한다
    // 연속 요소가 있으면 answer를 1 증가시키고, 연속 요소는 제거한다
    // 시간복잡도: O(N), 공간복잡도: O(N)

    Set<Integer> set = new HashSet<>();
    for (var num : nums) {
      set.add(num);
    }
    var answer = 0;
    for (var num : nums) {
      var length = 1;

      if (set.contains(num-1)) {
        set.remove(num);
        var minusKey = num;
        while (set.contains(--minusKey)) {
          length++;
          set.remove(minusKey);
        }
      }

      if (set.contains(num+1)) {
        set.remove(num);
        var plusKey = num;
        while (set.contains(++plusKey)) {
          length++;
          set.remove(plusKey);
        }
      }

      if (length > answer) {
        answer = length;
      }
    }

    return answer;
  }
}
