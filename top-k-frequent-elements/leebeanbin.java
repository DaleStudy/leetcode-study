import java.util.HashMap;
import java.util.Map;

public class Solution {
	public int[] topKFrequent(int[] nums, int k) {
		Map<Integer, Integer> map = new HashMap<>();

		// count how many duplicated numbers in the input array
		for (int num : nums) {
			map.put(num, map.getOrDefault(num, 0) + 1);
		}

		return map.entrySet().stream().sorted((a, b) -> b.getValue() - a.getValue()).limit(k)
				.mapToInt(Map.Entry::getKey).toArray();
	}
}
