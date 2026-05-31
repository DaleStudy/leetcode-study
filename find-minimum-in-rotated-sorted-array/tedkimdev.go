// TC: O(log n)
// SC: O(1)
func findMin(nums []int) int {
	min := nums[0]
	l, r := 0, len(nums)-1

	for l <= r {
			if nums[l] < min {
				min = nums[l]
			}
			break
		}

		m := l + (r-l)/2
		if nums[m] < min {
			min = nums[m]
		}

		if nums[m] >= nums[l] {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return min
}
