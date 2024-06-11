# Intuition
전형적인 이분탐색 문제였다.

# Approach
1. `nums[0]보다 작은지 여부`를 검사하도록 설계했다.
2. `lo`는 항상 F이며, `hi`는 항상 T이다.
2. 배열의 원소들에 대해 FFFFFFFTTTTTT가 되는데, 이 때 `T`가 처음 등장하는 지점을 찾는다.
3. 등장하지 않는 경우 (`nums[0]`이 최소인 경우 = 회전이 없는 경우)는 hi가 배열 범위 밖이므로, 인덱스 0을 반환하게 했다.

(문제 해결 이후 타 문제 재활용을 위해 인덱스를 찾도록 리팩터링했다.)
# Complexity
- Time complexity: $O(log(n))$
    - 배열의 길이 `n`에 대하여, 범위를 반으로 줄여가며 이분 탐색하므로 `log(n)`이 발생한다.

- Space complexity: $O(n), inline$
    - 배열의 길이 `n`에 대하여, 입력(`nums`)의 비용이 존재한다.

# Code
```go
func findMinIdx(nums []int) int {
	lo, hi := -1, len(nums)
	for lo+1 < hi {
		mid := (lo + hi) / 2

		if nums[mid] < nums[0] {
			hi = mid
		} else {
			lo = mid
		}
	}
	if hi == len(nums) {
		return 0
	}
	return hi
}

func findMin(nums []int) int {
	return nums[findMinIdx(nums)]
}

```

# 여담
이분탐색 문제는 타 솔루션을 참고하지 않는 편이다. 왜냐하면 `lo`, `hi`, 종료 조건, 반환 값 설정이 비슷해보이지만 엄청 다른 의미이기에 큰 도움이 안된다고 생각한다.