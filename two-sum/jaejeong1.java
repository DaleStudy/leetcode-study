import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class SolutionTwoSum {
  public int[] twoSum(int[] nums, int target) {
    // 모든 수를 해시맵에 저장한다. key = nums[i], value = i
    // 해시맵을 순회하며 target - key = result를 만족하는 쌍을 찾음
    // key 와 result 의 value를 정답으로 반환한다
    // 시간복잡도: O(N), 공간복잡도: O(N)
    // 값별 인덱스 리스트를 저장할 해시맵
    HashMap<Integer, List<Integer>> indicesByValue = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      indicesByValue.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
    }

    for (int key : indicesByValue.keySet()) {
      int diff = target - key;

      if (indicesByValue.containsKey(diff)) {
        int index1 = indicesByValue.get(key).get(0);

        // 동일한 값에 대해 두 개의 다른 인덱스가 있는지 확인
        int index2 = (key == diff && indicesByValue.get(key).size() > 1)
            ? indicesByValue.get(key).get(1)
            : indicesByValue.get(diff).get(0);

        return new int[]{index1, index2};
      }
    }

    // 쌍을 찾지 못한 경우
    return null;
  }
}