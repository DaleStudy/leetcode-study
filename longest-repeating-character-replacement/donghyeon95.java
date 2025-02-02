import java.util.HashMap;
import java.util.Map;
import java.util.Set;

class Solution {
	public int characterReplacement(String s, int k) {
		// K개까지는 용인되는 최대 길이를 구해라
		// 2 포인터 => 최대 O(2*N) = O(N)
		// 용인 되는 길이면 second++, 용인되는 길이가 아니면 first++;

		String[] strings = s.split("");
		HashMap<String, Integer> strCnt = new HashMap<>();
		int result = 0;
		int first = 0;
		int second = 0;

		while(first<s.length()){
			strCnt.put(strings[first], strCnt.getOrDefault(strings[first], 0)+1);
			System.out.println(" second: " + second + " first: " + first );
			if (getOtherCnt(strCnt) <= k) {
				result = Math.max(result, first-second+1);
				first++;
			}
			else {
				strCnt.put(strings[second], strCnt.getOrDefault(strings[second],1)-1);
				strCnt.put(strings[first], strCnt.getOrDefault(strings[first], 0)-1);
				second++;
			}
		}

		return result;
	}

	public int getOtherCnt(HashMap<String, Integer> strCnt) {
		int total = 0;
		int max = 0;
		for (int a: strCnt.values()) {
			total += a;
			max = Math.max(max, a);
		}
		return total - max;
	}
}


