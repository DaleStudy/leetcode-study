import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count each number's frequency using a hash map.
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Keep the top k numbers in a min-heap ordered by frequency.
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(freq.get(a), freq.get(b))
        );

        for (int num : freq.keySet()) {
            if (heap.size() < k) {
                heap.offer(num);
            } else if (freq.get(num) > freq.get(heap.peek())) {
                // Replace the least frequent number.
                heap.poll();
                heap.offer(num);
            }
        }

        // Return the numbers in the heap.
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll();
        }

        return result;
    }
}

// Time Complexity: O(n + u log k)
// Space Complexity: O(u + k)
// n = nums.length, u = number of unique numbers
