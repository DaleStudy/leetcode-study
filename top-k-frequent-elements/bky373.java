/**
 * time: O(N log k)
 * space: O(N + k)
 *
 * - time: N 개를 순회하며 heap 에 요소 추가, 최대 k 개만큼 요소를 추가하여 log k 만큼 시간이 곱해짐.
 * - space: 빈도 수를 저장하기 위해 N, 힙에 요소를 저장하기 위해 K 만큼 저장 공간을 사용함.
 */
class Solution {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int n : nums) {
            freqMap.put(n, freqMap.getOrDefault(n, 0) + 1);
        }
        Queue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(freqMap::get));
        for (Integer n : freqMap.keySet()) {
            pq.add(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return IntStream.range(0, k)
                        .map(i -> pq.poll())
                        .toArray();
    }
}
