import java.util.HashMap;
import java.util.Map;
class Solution {
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> myMap = new HashMap<>();
        for (int num : nums) {
            myMap.put(num, myMap.getOrDefault(num, 0) + 1);
        }
        return myMap.entrySet()
                .stream()
                .sorted((v1, v2) -> Integer.compare(v2.getValue(),v1.getValue()))
                .map(Map.Entry::getKey)
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
