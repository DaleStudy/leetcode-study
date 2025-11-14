import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Set<Integer> unique = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        Map<Integer, Integer> value = new HashMap<>();
        for (int n : unique) {
            int cnt = 0;
            for (int m : nums) {
                if (n == m) {
                    cnt++;
                }
            }
            value.put(n, cnt);
        }
        List<Map.Entry<Integer, Integer>> sortedByValueDesc = value.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .toList();
        return sortedByValueDesc.stream()
                .limit(k)
                .map(Map.Entry::getKey)
                .mapToInt(Integer::intValue)
                .toArray();
    }
}