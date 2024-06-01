# Intuition
0의 등장 횟수에 따라 경우의 수가 달라진다. 이를 이용한다.
# Approach
(사이트에서 Wrong Case를 제공하였기에 다양한 경우의 수를 대응할 수 있었다, 좋은 풀이는 아니라고 생각한다.)
- 모든 수의 곱을 계산한 후, 배열을 순회하며 자기 자신을 나눈 값을 저장한다.
- 0이 등장한 경우, 0이 아닌 배열의 원소들은 무조건 0을 저장해야 한다.
  - `golang`의 경우 `int`의 기본값이 0이라 아무것도 안해주면 된다.
- 0이 2회 이상 등장한 경우, 모든 원소는 0이 된다.
    - `golang`의 경우 길이만 선언된 `int` 배열을 반환하면 된다.
# Complexity
- Time complexity: $$O(n)$$
  - 배열의 길이 n에 대하여, 순회하는 비용 n이 발생한다.

- Space complexity: $$O(n)$$
  - 배열의 길이 n에 대하여, 결과를 저장할 배열의 크기 n이 소모된다.
# Code
```go
func productExceptSelf(nums []int) []int {
	answer := make([]int, len(nums))
	product := 1
	zeroCnt := 0
	for _, num := range nums {
		if num == 0 {
			zeroCnt++
			continue
		}
		product *= num
	}

	if zeroCnt >= 2 {
		product = 0
	}

	for i, num := range nums {
		if num == 0 {
			answer[i] = product
		} else if zeroCnt == 0 {
			answer[i] = product / num
		}
	}
	return answer
}
```