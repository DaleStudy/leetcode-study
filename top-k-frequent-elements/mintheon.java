import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;

class Solution {
  public int[] topKFrequent(int[] nums, int k) {
    int[] answer = new int[k];
    Map<Integer, Integer> frequent = new HashMap<>();

    for(int num: nums) {
      frequent.put(num, frequent.getOrDefault(num, 1) + 1);
    }

    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue().compareTo(a.getValue()));
    pq.addAll(frequent.entrySet());

    for(int i = 0; i < k; i++) {
      answer[i] = pq.poll().getKey();
    }

    return answer;
  }
}
