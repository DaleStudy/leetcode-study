// TC: O(n^2)
// SC: O(m)
func threeSum(nums []int) [][]int {
	result := make(map[[3]int]struct{})

	sort.Ints(nums)

	// target value = nums[k]
	for k := 0; k < len(nums); k++ {
		left := 0
		if k == left {
			left = 1
		}
		right := len(nums) - 1
		if k == right {
			right = len(nums) - 2
		}

		target := nums[k]
		for left < right {
			sum := nums[left] + nums[right] + target
			if sum == 0 {
				if left > k {
					result[[3]int{nums[k], nums[left], nums[right]}] = struct{}{}
				} else if left < k && k < right {
					result[[3]int{nums[left], nums[k], nums[right]}] = struct{}{}
				} else if k > right {
					result[[3]int{nums[left], nums[right], nums[k]}] = struct{}{}
				}
			}
			if sum < 0 {
				left++
				if k == left {
					left++
				}
			} else {
				right--
				if k == right {
					right--
				}
			}
		}

	}

	filteredResult := [][]int{}
	for k, _ := range result {
		filteredResult = append(filteredResult, k[0:len(k)])
	}

	return result.keys()
}
