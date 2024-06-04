# Intuition
자기 자신 이후에 몇 개가 연속되었는지를 `dp`로 저장한다.
# Approach
1. 등장 여부를 `appear`에 기록한다.
2. 자기 자신 이후 연속된 원소의 개수를 반환하는 함수를 만들고 매 배열마다 이를 호출한다.
    - `dp`로써, 자기 자신(`from`)에 따른 결과들을 유지한다.
    - 자기 자신이 등장했는지 여부에 따라 `0` 혹은 `다음 연속 개수 + 1`을 반환한다. 
3. 호출 결과 중 최대를 찾아 반환한다.
# Complexity
- Time complexity: $$O(nlog(n))$$

- Space complexity: $$O(n+m)$$
# Code
## Original
```go
func longestConsecutiveFrom(num int, appear map[int]bool, cache map[int]int) (ret int) {
	if val, ok := cache[num]; ok {
		return val
	}

	if _, ok := appear[num]; ok {
		ret = longestConsecutiveFrom(num+1, appear, cache) + 1
	} else {
		ret = 0
	}
	cache[num] = ret
	return ret
}

func longestConsecutive(nums []int) int {
	appear := make(map[int]bool, len(nums)/2)
	cache := make(map[int]int, len(nums)/2)
	for _, num := range nums {
		appear[num] = true
	}

	var max int

	for _, num := range nums {
		ret := longestConsecutiveFrom(num, appear, cache)
		if ret > max {
			max = ret
		}
	}
	return max
}
```

## Bottom-up
```go
func longestConsecutive(nums []int) int {
	appear := make(map[int]bool, len(nums)/2)
	for _, num := range nums {
		appear[num] = true
	}

	var max int

	for _, num := range nums {
		if appear[num-1] {
			continue
		}
		len := 1
		for appear[num+len] {
			len++
		}

		if len > max {
			max = len
		}
	}
	return max
}

```