/**
 * Constraints
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * k is in the range [1, the number of unique elements in the array].
 * It is guaranteed that the answer is unique.
 *
 * Output
 * - int 배열
 */

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // (1) HashMap + PriorityQueue
        // 시간복잡도 : O(N log N)
        // Runtime : 15ms Beats 38.03%
        // Memory : 48.93MB Beats 20.01%
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(Comparator.comparingInt(Map.Entry::getValue));

        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = minHeap.poll().getKey();
        }

        return result;

        // (2) Stream
        // 시간복잡도 : O(N log N)
        // Runtime : 19ms Beats 8.16%
        // Memory : 49.00MB Beats 20.01%
        // Stream에 익숙해지기 위해 공부용
        return Arrays.stream(nums)
                .boxed()
                .collect(Collectors.groupingBy(num -> num, Collectors.summingInt(num -> 1)))
                .entrySet().stream()
                .sorted((a, b) -> b.getValue() - a.getValue())
                .limit(k)
                .mapToInt(Map.Entry::getKey)
                .toArray();

        // (3) Array List
        // 시간복잡도 : O(N)
        // Runtime : 13ms Beats 75.77%
        // Memory : 48.44MB Beats 61.68%
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new List[nums.length + 1];
        for (int key : frequencyMap.keySet()) {
            int freq = frequencyMap.get(key);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(key);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = buckets.length - 1; i >= 0 && result.size() < k; i--) {
            if (buckets[i] != null) {
                result.addAll(buckets[i]);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}