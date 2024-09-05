func dfs(s string, i int, memo map[int]int) int {
	if i == len(s) {
		return 1
	}
	if val, found := memo[i]; found {
		return val
	}
	if s[i] == '0' {
		memo[i] = 0
		return 0
	}

	// 1자리 숫자로 디코딩
	result := dfs(s, i+1, memo)

	// 2자리 숫자로 디코딩
	if i+1 < len(s) {
		// 10의 자리 숫자 또는 20의 자리 숫자로 디코딩
		if (s[i] == '1') || (s[i] == '2' && s[i+1] >= '1' && s[i+1] <= '6') {
			result += dfs(s, i+2, memo)
		}
	}
	// dp에 저장
	memo[i] = result
	return result
}

func numDecodings(s string) int {
	// memo 테이블 만들고 dfs 호출
	memo := make(map[int]int)
	return dfs(s, 0, memo)
}
