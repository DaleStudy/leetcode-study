import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
	/*
	 * @param strs: a list of strings
	 * @return: encodes a list of strings to a single string.
	 */
	String cDel = "&";
	String sDel = ";";

	// Encodes a list of strings to a single string
	public String encode(List<String> strs) {
		if (strs.isEmpty()) return null;

		StringBuilder result = new StringBuilder();
		for (int i =0; i<strs.size(); i++) {
			String str = strs.get(i);
			StringBuilder temp = new StringBuilder();
			for (char c : str.toCharArray()) {
				temp.append((int) c).append(cDel);
			}

			result.append(temp);
			if (i != strs.size()-1)  result.append(sDel);
		}
		return result.toString();
	}

	// Decodes a single string to a list of strings
	public List<String> decode(String str) {
		if (str==null)
			return new ArrayList<>();

		List<String> result = new ArrayList<>();
		String[] strs = str.split(sDel, -1);
		for (String s : strs) {
			if (s.isEmpty()) {
				result.add("");
				continue;
			}
			String[] chars = s.split(cDel);
			String decoded = Arrays.stream(chars)
				.filter(sr -> !sr.isEmpty())
				.mapToInt(Integer::parseInt)
				.mapToObj(ascii -> (char) ascii)
				.map(String::valueOf)
				.collect(Collectors.joining());
			result.add(decoded);
		}
		return result;
	}
}


