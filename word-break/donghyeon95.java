import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
	public boolean wordBreak(String s, List<String> wordDict) {
		return dfs(s, wordDict, new HashSet<>());
	}

	private boolean dfs(String s, List<String> wordDict, Set<String> dp) {
		// 종료 조건: 문자열이 비어 있으면 성공
		if (s.isEmpty()) return true;

		// 중복 탐색 방지
		if (dp.contains(s)) return false;

		for (String word : wordDict) {
			if (s.startsWith(word)) {
				// 단어를 제거하고 재귀 호출
				if (dfs(s.substring(word.length()), wordDict, dp)) {
					return true;
				}
			}
		}

		// 단어를 제거하지 않고 넘어가는 경우도 탐색
		dp.add(s); // 탐색이 실패한 상태 저장
		return false;
	}
}



