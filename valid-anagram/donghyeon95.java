import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

class Solution {
	public boolean isAnagram(String s, String t) {
		boolean result = false;

		char[] chars = s.toCharArray();
		Map<Character, Integer> counter = new HashMap<>();
		for (char c: chars) {
			counter.put(c, counter.getOrDefault(c, 0)+1);
		}

		char[] tChars = t.toCharArray();
		for (char c: tChars) {
			if (!counter.containsKey(c)) return false;
			counter.put(c, counter.get(c)-1);

			if (counter.get(c) == 0)
				counter.remove(c);
		}

		return counter.isEmpty();
	}
}

