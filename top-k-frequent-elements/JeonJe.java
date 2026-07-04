import java.util.*;

// TC: O(n log n)
// SC: O(n)
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            Integer freq = map.getOrDefault(num, 0);
            map.put(num, freq + 1);
        }

        List<Map.Entry<Integer, Integer>> freqList = new ArrayList<>(map.entrySet());

        return freqList.stream()
                .sorted(Comparator.comparing(Map.Entry::getValue, Comparator.reverseOrder()))
                .map(Map.Entry::getKey)
                .limit(k)
                .mapToInt(Integer::intValue)
                .toArray();

    }
}
