import java.util.HashMap;

class Solution {
	public int lengthOfLongestSubstring(String s) {
		// subString을 찾아야 한다.
		// for 문을 반복하면서 내가 가지고 있는 문자열에 있는 문자라면
		// 그 문자열까지의 길이를 기록하고 꼬리를 짜르고 다시 반복문
		int result = 0;
		HashMap<String, Boolean> hm = new HashMap<>();
		StringBuilder nowString = new StringBuilder();

		for (String charater: s.split("")) {
			System.out.println(charater);
			if (hm.containsKey(charater)) {
				// nowString
				int index = nowString.indexOf(charater);
				nowString = new StringBuilder(nowString.substring(index+1) + charater);
				result = Math.max(nowString.length(), result);
				String removedString = nowString.substring(0, index);
				// String의 길이는 최대 27 * n
				for (String c: removedString.split("")) {
					hm.remove(c);
				}
			}
			else {
				hm.put(charater, true);
				nowString.append(charater);
			}
		}


		return Math.max(nowString.length(), result);
	}
}



