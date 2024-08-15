import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class SolutionJaeJeong1 {
  public boolean containsDuplicate(int[] nums) {
    // 해시맵 사용해서 같은 값의 카운트가 1보다 크면 true 반환
    // 끝까지 다 돌면 false 반환
    // 또는 해시셋 사용해서 모두 해시셋에 넣고
    // 길이 비교해서 같으면 false, 다르면 true 반환
    // 시간복잡도: O(N), 공간복잡도: O(N)

    Set<Integer> set = Arrays.stream(nums).collect(HashSet::new, Set::add, Set::addAll);
    return set.size() != nums.length;
  }
}