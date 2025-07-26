import java.util.*;


class Solution {
    /* 시간 복잡도: O(N + M * log k)
    * - for 루프: O(N), frequency 구하기
    * - for 루프: O(M * log k), Map 순회
        - Map 요소: M개
    *   - PriorityQueue 연산 (offer, poll): 평균 O(logk)
    * 
    * 공간 복잡도: O(N + k), HashMap에 n개 + PriorityQueue에 k개
    */ 
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        // [num, frequency]
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((o1, o2) -> {
            return o1[1] - o2[1];
        });
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        for (var entry: frequencyMap.entrySet()) {
            minHeap.add(new int[]{entry.getKey(), entry.getValue()});
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = minHeap.poll()[0];
        }
        return answer;
    }
}

