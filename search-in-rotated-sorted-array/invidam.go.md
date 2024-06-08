# Intuition
이분 탐색인 게 직관적으로 보였다.

# Approach
1. 찾으려는 값(`target`)이 최솟값의 인덱스(`minIdx`) 이전/이후인지 판단한다. (`target < nums[0] || minIdx == 0`)
2. 판단한 범위(이전, 이후)에 대해서만 배열을 잘라 `lowerBound`를 실행한다.
3. 결과를 통해 타겟의 인덱스(`targetIdx`)를 획득한다.
4. 예외처리(범위 벗어난 경우, `lowerBound`은 맞으나 일치하진 않는 경우)엔 `-`을 아닌 경우는 인덱스를 반환한다.

# Complexity
- Time complexity: $O(log(n))$
    - 배열의 길이 `n`에 대하여, 범위를 반으로 줄여가며 이분 탐색하므로 `log(n)`이 발생한다.
    - 두 이분탐색 함수를 사용하긴 하지만, 합연산이므로 복잡도에는 영향이 없다.
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

func lowerBound(nums []int, target int) int {
	lo, hi := -1, len(nums)
	for lo+1 < hi {
		mid := (lo + hi) / 2

		if nums[mid] < target {
			lo = mid
		} else {
			hi = mid
		}
	}
	return hi
}

func search(nums []int, target int) int {
	minIdx := findMinIdx(nums)
	var targetIdx int
	if target < nums[0] || minIdx == 0 {
		targetIdx = lowerBound(nums[minIdx:], target) + minIdx
	} else {
		targetIdx = lowerBound(nums[0:minIdx], target)
	}

	if len(nums) <= targetIdx || target != nums[targetIdx] {
		return -1
	}
	return targetIdx

}

```