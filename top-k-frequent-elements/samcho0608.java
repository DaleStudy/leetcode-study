import java.util.*;

// Time complexity: O(Nlogk)
// Space complexity: O(N)
class Solution1 {
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

// Time complexity: O(N)
// Space complexity: O(N)
class Solution2 {
    public int[] topKFrequent(int[] nums, int k) {
        // count frequencies
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // bucket: index = frequency, value = list of numbers
        List<List<Integer>> buckets = new ArrayList<>(nums.length + 1);
        for (int i = 0; i <= nums.length; i++) {
            buckets.add(new ArrayList<>());
        }

        for (var entry : freq.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            buckets.get(count).add(num);
        }

        // gather top k frequent elements
        int[] result = new int[k];
        int idx = 0;
        for (int i = nums.length; i >= 0 && idx < k; i--) {
            for (int num : buckets.get(i)) {
                result[idx++] = num;
                if (idx == k) break;
            }
        }

        return result;
    }
}
