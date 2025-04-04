import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class runnz121 {

    public class Solution {

        public int[] topKFrequent(int[] nums, int k) {

            Map<Integer, Integer> map = new HashMap<>();

            for (int i = 0; i < nums.length; i++) {
                map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            }

            PriorityQueue<Integer> maxPq = new PriorityQueue<>(
                    (a, b) -> map.get(b) - map.get(a)
            );

            maxPq.addAll(map.keySet());

            int[] result = new int[k];

            for (int i = 0; i < k; i++) {
                result[i] = maxPq.poll();
            }
            return result;
        }
    }
}
