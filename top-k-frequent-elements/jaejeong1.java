import java.util.HashMap;
import java.util.Map;

class SolutionTopKFrequentElements {
  public int[] topKFrequent(int[] nums, int k) {
    // 빈도순으로 k개 반환
    // 빈도 체크: 해시맵으로 카운트. 시간복잡도 O(N), 공간복잡도 O(N)
    // 빈도순 정렬: sorting, 시간복잡도 O(N log N), 공간복잡도 O(N)
    // 합산: 시간복잡도 O(N log N), 공간복잡도 O(N)

    // 빈도 체크
    Map<Integer, Integer> freq = new HashMap<>();
    for (int num : nums) {
      freq.put(num, freq.getOrDefault(num, 0) + 1);
    }

    // 빈도순 정렬
    return freq.keySet().stream()
      .sorted((a, b) -> freq.get(b) - freq.get(a))
      .mapToInt(i -> i)
      .limit(k) // 배열에서 상위 k개만 반환
      .toArray();
  }
}
