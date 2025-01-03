import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
	private HashMap<Integer, List<String>> dp = new HashMap<>();
	private HashSet<Integer> set;

	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		set = new HashSet<>(Arrays.stream(candidates).boxed().toList());
		recurse(target);
		// Convert dp entries back to List<List<Integer>> for return
		return dp.getOrDefault(target, new ArrayList<>()).stream()
			.map(str -> Arrays.stream(str.split(" "))
				.map(Integer::valueOf)
				.collect(Collectors.toList()))
			.collect(Collectors.toList());
	}

	public void recurse(int target) {
		if (dp.containsKey(target)) return;

		List<String> combinations = new ArrayList<>();
		for (int i = 1; i < target + 1; i++) {
			if (set.contains(i)) {
				int remaining = target - i;
				recurse(remaining);
				if (dp.containsKey(remaining)) {
					for (String combination : dp.get(remaining)) {
						List<Integer> newCombination = new ArrayList<>(Arrays.stream(combination.split(" "))
							.map(Integer::valueOf)
							.toList());
						newCombination.add(i);
						newCombination.sort(Comparator.reverseOrder());

						String newCombinationStr = newCombination.stream()
							.map(String::valueOf)
							.collect(Collectors.joining(" "));
						if (!combinations.contains(newCombinationStr)) {
							combinations.add(newCombinationStr);
						}
					}
				}
			}
		}
		if (set.contains(target)) {
			String singleCombination = String.valueOf(target);
			if (!combinations.contains(singleCombination)) {
				combinations.add(singleCombination);
			}
		}
		dp.put(target, combinations);
	}

}

