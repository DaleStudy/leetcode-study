# Intuition
비트 연산자를 활용하여 계산한다.
# Approach
1. `n`과 비교하기 위한 `mask`를 생성한다.
2. `mask`를 2진수 `1`, `10`, `100` 순으로 증가시킨 후  `&` 연산자를 활용해,  n의 특정 비트가 `1`인지 판단한다.
3. 참인 경우 `cnt`를 증가시켜 결과를 구한다.

# Complexity
- Time complexity: $$O(logn)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
: `mask`가 있는 반복문에 의해 결정된다. `mask`는 입력으로 들어온 `n`까지 2배씩 증가하므로 $$O(logn)$$이다.
- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
: 별도 자료구조를 사용하지 않는다.
# Code
```go
func hammingWeight(n int) int {
	cnt := 0
	for mask := 1; mask <= n; mask = mask << 1 {
		if (mask & n) != 0 {
			cnt += 1
		}
	}
	return cnt
}
```

# What I learned
- 고언어에서 첫 비트 연산자 활용