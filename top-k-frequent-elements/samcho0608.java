import java.util.*;

class Solution {
    // return: top k most freq elements
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        // O (N)
        for(int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1); // O(1)
        }

        // O (N log k)
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        for(int num : freq.keySet()) {
            int f = freq.get(num); // O(1)
            heap.add(new int[]{num, f}); // O(log k)

            if(heap.size() > k) heap.poll(); // O(log k)
        }

        // O (N log k)
        int[] result = new int[k];
        for(int i = 0; i < k; i++) {
            result[i] = heap.poll()[0]; // O(log k)
        }

        return result;
    }
}
