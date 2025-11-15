import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

class SolutionTopKFrequentElements {
  public int[] topKFrequent(int[] nums, int k) {
      // 풀이
      // 시간복잡도: O(N log K), 공간복잡도: O(N)

      // 숫자 별 빈도 누적을 Map 이용
      // 시간복잡도: O(N), 공간복잡도: O(N)
      Map<Integer, Integer> count = new HashMap<>();
      for (int n: nums) {
          count.put(n, count.getOrDefault(n, 0) + 1);
      }

      Queue<Integer> heap = new PriorityQueue<>((x, y) -> count.get(x) - count.get(y));
      // 가장 빈번한 k개의 수를 만들기 위해 우선순위 큐를 사용
      // 시간복잡도: O(N log k), 공간복잡도: O(N)
      for (int n: count.keySet()) {
          heap.add(n);
          if (heap.size() > k) heap.poll(); // 가장 빈번한 K개가 만족됐으니 더이상 추가하지 않고 제외
      }

      // k ~ 0 순서대로 힙에서 역순으로 뽑음
      // 시간복잡도: O(k log k), 공간복잡도: O(N)
      int[] result = new int[k];
      for(int i = k - 1; i >= 0; --i){
          result[i] = heap.poll();
      }

      return result;
  }
}
