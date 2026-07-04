import java.util.*;

class Solution {
    static class Item implements Comparable<Item> {
        int num;
        int count;

        Item(int num, int count) {
            this.num = num;
            this.count = count;
        }

        @Override
        public int compareTo(Item other) {
            return Integer.compare(other.count, this.count);
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Item> queue = new PriorityQueue<>();
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            queue.add(new Item(entry.getKey(), entry.getValue()));
        }

        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = queue.poll().num;
        }

        return answer;
    }
}
