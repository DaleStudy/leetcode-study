import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
	public List<List<String>> groupAnagrams(String[] strs) {
		// 문자열 정렬을 해서 같은 애들 모음을 주면 되지 않을까??
		// 이럴 경우 정렬에 많은 시간을 소모

		HashMap<String, List<String>> hm = new HashMap<>();
		for (String str: strs) {
			String arrangedStr = rearangeStr(str);
			hm.putIfAbsent(arrangedStr, new ArrayList<>());
			hm.get(arrangedStr).add(str);
		}

		return hm.values().stream().toList();
	}

	public String rearangeStr (String str) {
		char[] chars = str.toCharArray();
		Arrays.sort(chars);

		return new String(chars);
	}
}

