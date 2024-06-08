# Intuition
DP, 그리디 등을 시도하려다가 오류를 발견했다. 화이트보드에 예제 문제들을 손으로 풀어보니 직관적으로 떠올랐다.
# Approach
1. 똑같은 음식을 먹지 않는 지렁이를 생각하자.
2. 다음 음식을 이미 먹었다면, 먹었던 걸 뱉는다. (`l++`)
3. 다음 음식을 먹지 않았다면, 먹는다. (`r++`)
4. 지렁이의 길이를 최댓값 갱신에 활용한다.
# Complexity
- Time complexity: $O(n)$
    - 문자열의 길이 `n`에 대하여, 이를 순회하는 비용이 소모된다.
- Space complexity: $O(n)$
    - 문자열의 길이 `n`에 대하여, 등장 여부를 저장하는 자료구조(`contains`)는 최대 `n`개 만큼을 저장할 수 있으므로 `n`이다.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```go
func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	contains := make(map[uint8]bool)

	l, r := 0, 0
	maxLen := 1

	for r < len(s) {
		for contains[s[r]] {
			contains[s[l]] = false
			l++
		}
		contains[s[r]] = true
		maxLen = max(maxLen, r-l+1)
		r++
	}

	return maxLen
}

```