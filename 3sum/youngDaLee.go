package youngDaLee

import (
	"fmt"
	"slices"
)

func threeSum(nums []int) [][]int {
	// sort nums
	slices.Sort(nums)

	// unique-ify nums
	uniqueKeys := make(map[string]bool)

	var result [][]int
	left := 0
	for left < len(nums)-2 {
		// init pivot, right
		pivot := left + 1
		right := len(nums) - 1

		for pivot < right {
			sum := nums[left] + nums[pivot] + nums[right]
			unikeyKey := fmt.Sprintf("%d%d%d", nums[left], nums[pivot], nums[right])
			if sum == 0 {
				if _, ok := uniqueKeys[unikeyKey]; !ok {
					uniqueKeys[unikeyKey] = true
					result = append(result, []int{nums[left], nums[pivot], nums[right]})
				}
				for pivot < right-1 && nums[pivot] == nums[pivot+1] {
					pivot += 1
				}
				for pivot < right-1 && nums[right] == nums[right-1] {
					right -= 1
				}
				pivot += 1
				right -= 1
			} else if sum < 0 {
				pivot += 1
			} else if sum > 0 {
				right -= 1
			}
		}

		left += 1
		for left < len(nums)-2 && nums[left] == nums[left-1] {
			left += 1
		}
	}
	return result
}
