import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // time complexity O(n)
        // space complexity O(n)

        HashMap<Integer, Integer> frequentMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            frequentMap.merge(num, 1, Integer::sum);
        }

        ArrayList<Integer>[] buckets = new ArrayList[nums.length + 1];

        for (int i = 0; i <= nums.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        frequentMap.forEach((Integer a, Integer b) -> {
            // Assign the largest values from the front of the array
            buckets[nums.length - b].add(a);
        });

        int[] result = new int[k];

        int pointer = 0;

        for (int i = 0; i < buckets.length; i++) {
            ArrayList<Integer> list = buckets[i];
            if (list.size() == 0) {
                continue;
            }
            for (Integer num : list) {
                result[pointer] = (int) num;
                // Return the result when the pointer reaches k
                if (pointer == (k - 1))
                    return result;
                pointer++;
            }
        }

        return result;
    }
}