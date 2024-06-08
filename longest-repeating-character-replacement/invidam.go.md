# Intuition
문자열 내에 영문자들만 등장한다는 것에서 DP, 그리디가 아니라 빈도수 계산 + 투포인터임을 알게되었다.

# Approach
1. A-Z에 대해 순회한다.
2. 포함하는 배열이 커지며(`j++`) 순회하는 문자가 몇 번 연속해서 등장하는지 계산한다. (`have`)
3. 연속하지 않은 문자가 등장하더라도 `k`번은 봐준다.
4. `k`번이상이라 봐줄 수 없는 경우 (`have+k < j-i+1`인 경우) 포함하는 배열을 줄인다. (`i++`)

# Complexity
- Time complexity: $O(n)$
    - 순회하는 문자들은 상수 개수(26)이므로 무시한다.
    - 문자열의 길이 `n`에 대하여, 이를 순회하는 비용이 든다. (`j<len(s)`)

- Space complexity: $O(n) inline$
    - 문자열의 길이 `n`에 대하여, 입력으로 받은 `s`만큼 비용이 든다.

# Code
```go
func characterReplacement(s string, k int) int {
	var maxLen int
	for ch := 'A'; ch <= 'Z'; ch++ {
		i, j := 0, 0
		var have int
		for j < len(s) {
			if ch == rune(s[j]) {
				have++
			}
			for have+k < j-i+1 {
				if ch == rune(s[i]) {
					have--
				}
				i++
			}
			maxLen = max(maxLen, j-i+1)
            j++
		}
	}
	return maxLen
}

```
# 여담
- 가장 많이 등장한 문자를 검색하는 솔루션을 확인했다. 동일 문제를 다르게 접근한다는 게 신기했다.
  - 비교해보자면, A~Z중 한 문자가 등장하는 것만 계산한다는 본인의 풀이가 더욱 직관적이라는 생각이 들었다.
  - 다만, 코드로 나타냈을 때는 덜 직관적이었다...;