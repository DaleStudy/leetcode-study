// 문제 풀이 흐름
// 아나그램 : 글자 빈도가 같으면 항상 아나그램 관계
// 가장 먼저 : 전체 글자수가 같은지 비교
// 그 다음 -> 알파벳 별로 빈도수가 같은지 비교

// n = max(s의 길이, t의 길이)라고 했을때
// 시간복잡도 : O(n)
// 공간복잡도 : O(1)

class Solution {
	public boolean isAnagram(String s, String t) {
		int[] sCount = new int[26];
		int[] tCount = new int[26];

		if (s.length() != t.length()) return false;

		for (int i = 0 ; i < s.length() ; i++) {
			sCount[s.charAt(i) - 'a'] ++;
			tCount[t.charAt(i) - 'a'] ++;
		}

		for (int i = 0 ; i < 26 ; i++) {
			if (sCount[i] == tCount[i]) continue;
			return false;
		}

		return true;
	}
}
