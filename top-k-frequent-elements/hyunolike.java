class Solution {
    public int[] topKFrequent(int[] nums, int k) {
            Map<Integer, Integer> counter = new HashMap<>();
            for (int n : nums) {
                counter.put(n, counter.getOrDefault(n, 0) + 1);
            }

            PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
                (a, b) -> Integer.compare(b.getValue(), a.getValue())
            );

            for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
                heap.offer(entry);
            }

            int[] res = new int[k];
            for(int i = 0; i < k; i++) {
                res[i] = Objects.requireNonNull(heap.poll()).getKey();
            }

            return res;
    }
}