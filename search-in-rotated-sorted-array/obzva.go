/*
풀이
- 이진탐색을 두 번 사용하여 풀이할 수 있습니다
  첫번째, pivot index를 찾습니다
  두번째, target을 찾습니다

Big O
- N: 주어진 배열 nums의 길이
- Time complexity: O(logN)
  - 각 이진탐색이 모두 O(logN)의 시간 복잡도를 가집니다
- Space complexity: O(1)
*/

func search(nums []int, target int) int {
	n := len(nums)

	lo, hi := 0, n
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] > nums[n-1] {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	pivot := lo
	if pivot == n {
		pivot = 0
	}

	lo, hi = pivot, pivot+n
	for lo < hi {
		mid := lo + (hi-lo)/2
		normalizedMid := mid
		if normalizedMid >= n {
			normalizedMid = mid - n
		}
		if nums[normalizedMid] <= target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	if lo > n {
		lo -= n
	}
	if lo-1 < 0 || nums[lo-1] != target {
		return -1
	}
	return lo - 1
}
