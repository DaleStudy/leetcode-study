/*
풀이
- 슬라이딩 윈도우를 이용하여 풀이합니다
- 주어진 문자열 t의 각 문자와 그 개수를 tMap이라는 해시맵에 저장합니다
- 현재 슬라이딩 윈도우에 포함된 문자와 그 개수를 sMap이라는 해시맵에 저장합니다
- 슬라이딩 윈도우의 끝단(end)을 넓혀나가면서 sMap과 tMap을 비교합니다
  이 때 슬라이딩 윈도우가 t의 모든 문자를 포함하는 경우를 찾으면 시작단(start)을 좁혀주면서  슬라이딩 윈도우의 최소폭을 찾습니다
    슬라이딩 윈도우가 t의 모든 문자를 포함하는지를 판별하기 위해서 match라는 변수를 사용합니다
    match는 sMap[c] == tMap[c]인 문자 c의 개수이며, match == len(tMap) 즉 match가 t의 고유 문자 개수와 같다면 슬라이딩 윈도우가 t의 모든 문자를 포함하는 것이라고 볼 수 있습니다
	슬라이딩 윈도우를 좁혀줄 때에도 match의 감소 여부를 잘 관찰하며 최소폭을 갱신합니다
	슬라이딩 윈도우를 줄일만큼 줄였다면 다시 슬라이딩 윈도우의 끝단을 넓혀나가면서 다른 경우의 수를 찾습니다

Big O
- M: 주어진 문자열 s의 길이
- N: 주어진 문자열 t의 길이
- Time complexity: O(M + N)
  - 문자열 s를 순회하는 반복문 내에서 각 문자는 최대 두 번 조회될 수 있습니다 (start, end) -> O(2M)
  - 문자열 t로 해시맵을 만드는 데에는 O(N)의 시간복잡도가 소요됩니다
  - O(2M + N) -> O(M + N)
- Space complexity: O(M + N)
  - 두 개의 해시맵을 사용하므로 O(M + N)의 공간복잡도를 갖습니다
*/

func minWindow(s string, t string) string {
	sMap, tMap := map[string]int{}, map[string]int{}
	for _, r := range t {
		tMap[string(r)]++
	}

	start, end, matched, res := 0, 0, 0, ""
	for end < len(s) {
		sMap[string(s[end])]++

		if sMap[string(s[end])] == tMap[string(s[end])] {
			matched++
		}

		for matched == len(tMap) {
			if res == "" || len(res) > end-start+1 {
				res = s[start : end+1]
			}

			if sMap[string(s[start])] == tMap[string(s[start])] {
				matched--
			}
			sMap[string(s[start])]--
			start++
		}

		end++
	}

	return res
}
