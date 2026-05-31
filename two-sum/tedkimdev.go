package hello

import "testing"

// Time complexity: O(n)
// Space complexity: O(n)
func twoSum(nums []int, target int) []int {
	indexByNum := map[int]int{}
	for i, num := range nums {
		diff := target - num
		if index, ok := indexByNum[diff]; ok {
			return []int{index, i}
		}
		indexByNum[num] = i
	}
	return []int{}
}

func TestTwoSome(t *testing.T) {

}
