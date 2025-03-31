import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

// 시간 복잡도: O(nlogk) - 최대 힙에 k개의 요소를 넣는데 O(logk)가 걸리고, 이를 n번 반복
// 공간 복잡도: O(n) - 빈도수를 저장하는 freqMap
class Solution {

  public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<Map.Entry<Integer, Integer>> maxHeap =
        new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

    // 빈도수를 기준으로 최소 힙에 k개의 요소를 넣기
    for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
      maxHeap.offer(entry);
    }

    int[] result = new int[k];
    int index = 0;
    while (k > 0) {
      k--;
      result[index++] = maxHeap.poll().getKey();
    }

    return result;
  }
}
