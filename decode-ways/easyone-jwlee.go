// 풀이
// dp로 풀이
// 두자리 수에 적합하면 prev2(i-2)에 해당하는 값을 더하기

// TC
// O(n)

// SC
// data type이 int인 변수만 사용했으므로 O(1)

func numDecodings(s string) int {
	if len(s) == 0 || s[0] == '0' {
		return 0
	}
	prev2, prev1 := 1, 1
	for i := 1; i < len(s); i++ {
		curr := 0

		// 한자리수 확인
		if s[i] != '0' {
			curr += prev1
		}

		// 두자리수 확인
		digit, _ := strconv.Atoi(s[i-1 : i+1])
		if digit >= 10 && digit <= 26 {
			curr += prev2
		}

		prev2, prev1 = prev1, curr
	}
	return prev1
}
