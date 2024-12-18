import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/*
	map에 넣고 빼는 시간이 O(n)이라고는 하나, 시간이 걸린다.
	반복문으로 처리할 수 있는 방법이 없을까?
*/

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

