# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
이전 값들을 재활용한다.
# Approach
<!-- Describe your approach to solving the problem. -->
1. 엣지 케이스는 0을 반환한다.
2. 0, 1을 미리 계산한다.
3. `>>`을 수행한 결과 + 짝/홀 여부로 인한 1을 더해서 해결해준다.
- 이진수 `1001`의 경우 `100` 계산한 결괏값에서 `1`을 더해주면 된다.
- 이진수 `1010`의 경우 `101` 계산한 결괏값에서 `0`을 더해주면 된다.

- 솔루션 참고: `i & (i-1)` 연산을 통해 계산한다.
    - 2의 제곱수인 경우 `0`이 나와 1을 더하면 된다.
    - 아닌 경우는 아직은 잘 모르겠다.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
:`n`크기의 배열을 모두를 순회한다.
- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
:크기 `n`의 배열을 선언한다.
# Code
```go
func countBits(n int) []int {
	if n == 0 {
		return []int{0}
	}
	ans := make([]int, n+1, n+1)

	ans[0], ans[1] = 0, 1

	for i := 2; i <= n; i++ {
		ans[i] = ans[i>>1] + i&1
	}
	return ans
}

func countBitsSolution(n int) []int {
	res := make([]int, n+1)
	for i := 1; i <= n; i++ {
		res[i] = res[i&(i-1)] + 1
	}
	return res
}
```