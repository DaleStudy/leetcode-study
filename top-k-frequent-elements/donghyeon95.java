import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
	public int[] topKFrequent(int[] nums, int k) {
		HashMap<Integer, Integer> hm = new HashMap<>();

		for (int num: nums) {
			hm.put(num, hm.getOrDefault(num, 0)+1);
		}

		List<Map.Entry<Integer, Integer>> list = new ArrayList<>(hm.entrySet());
		list.sort(Map.Entry.comparingByValue(Collections.reverseOrder()));

		int index = 1;
		ArrayList<Integer> answer = new ArrayList<>();
		for (Map.Entry<Integer, Integer> entry: list) {
			if (index > k) break;
			answer.add(entry.getKey());
			index++;
		}

		return answer.stream().mapToInt(Integer::intValue).toArray();
	}
}

