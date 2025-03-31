// 시간복잡도: O(n)
// 공간복잡도: O(1)

func maxProduct(nums []int) int {
	result, max, min := nums[0], 1, 1

	for _, num := range nums {
		candidates := []int{max * num, min * num, num}
		max = maxIntIn3(candidates[0], candidates[1], candidates[2])
		min = minIntIn3(candidates[0], candidates[1], candidates[2])
		if max > result {
			result = max
		}
	}

	return result
}

func maxIntIn3(a, b, c int) int {
	if a > b && a > c {
		return a
	}
	if b > c {
		return b
	}
	return c
}

func minIntIn3(a, b, c int) int {
	if a < b && a < c {
		return a
	}
	if b < c {
		return b
	}
	return c
}
