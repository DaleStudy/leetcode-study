# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
배타적인 경우에만 참을 출력하는 `XOR` 연산을 활용한다.
# Approach
<!-- Describe your approach to solving the problem. -->
- 문제를 치환해보자. 모든 수가 2번씩 등장하고, 하나의 수만 한 번 등장한다고 하자.
- 이 경우, 모든 수들에 `^`연산을 하면 한 번 등장한 수만을 알 수 있다.
- `배열의 길이` + `인덱스`와 `해당 인덱스일 때의 원소값`들을 모두 `^`연산하면
    - 배열 + 인덱스 순회로 모든 수는 1번씩 등장한다.
    - 원소값 순회로 하나의 수를 제외하곤 1번씩 등장한다.
- 한 번만 등장한 수가 missing number이다.
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
: 배열의 길이 `n`, 이를 순회한다.
- Space complexity: $$O(n)$$

  : inline, 주어진 배열의 길이 `n`
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```go
func missingNumber(nums []int) int {
	num := len(nums)

	for i, n := range nums {
		num ^= i
		num ^= n
	}
	return num
}
```

# Today I Learned
- 다른 풀이로 풀 때, `abs()`를 이용해서 해결하려고 하였는데 해당 라이브러리가 존재하지 않았다. 왜 그런지 찾아봤는데 너무 간단한 라이브러리는 철학에 안맞는다고 안넣어준다 하더라.
  - 참고: https://go.dev/doc/faq#x_in_std