// 시간복잡도: O(n)
// 공간복잡도: O(1)

package main

import "testing"

func TestMissingNumber(t *testing.T) {
	if missingNumber([]int{3, 0, 1}) != 2 {
		t.Error("Test case 0 failed")
	}

	if missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1}) != 8 {
		t.Error("Test case 1 failed")
	}
}

func missingNumber(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	
	target := len(nums) * (len(nums) + 1) / 2
	return target - sum
}
