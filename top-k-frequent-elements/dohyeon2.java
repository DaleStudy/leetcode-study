import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Comparator;

public class dohyeon2 {
    public int[] topKFrequent(int[] nums, int k) {
        // approach : 
        // 1. create map to match num to frequency
        // 2. create max frequency Priority Queue for sort
        // 3. pop the max value from the queue until k
        // time complexity O(n log n) : priority queue comparison
        // space complexity O(n)

        // ChatGPT says that there is O(n) solution for this, how?
        HashMap<Integer, Integer> frequentMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            frequentMap.merge(num, 1, Integer::sum);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> PQ = new PriorityQueue<>(k,
                Comparator.comparing(Map.Entry<Integer, Integer>::getValue).reversed());

        for(Map.Entry<Integer,Integer> e : frequentMap.entrySet()){
            PQ.add(e);
        }

        int[] result = new int[k];

        int idx = 0;

        while (idx < k && PQ.size() > 0) {
            Map.Entry<Integer, Integer> v = PQ.poll();
            result[idx] = (int) v.getKey();
            idx++;
        }

        return result;
    }
} 
