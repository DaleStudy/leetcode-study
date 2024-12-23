// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import "testing"

func TestTwoSum(t *testing.T) {
	result1 := twoSum([]int{2, 7, 11, 15}, 9)

	if len(result1) != 2 {
		t.Errorf("Expected 2, got %d", len(result1))
	}

	if result1[0] != 0 && result1[1] != 1 {
		t.Errorf("Expected [0, 1], got %v", result1)
	}

	result2 := twoSum([]int{3, 2, 4}, 6)

	if len(result2) != 2 {
		t.Errorf("Expected 2, got %d", len(result2))
	}

	if result2[0] != 1 && result2[1] != 2 {
		t.Errorf("Expected [1, 2], got %v", result2)
	}

	result3 := twoSum([]int{3, 3}, 6)
	if len(result3) != 2 {
		t.Errorf("Expected 2, got %d", len(result3))
	}

	if result3[0] != 0 && result3[1] != 1 {
		t.Errorf("Expected [0, 1], got %v", result3)
	}
}

func twoSum(nums []int, target int) []int {
	seen := map[int]int{}
	for i, num := range nums {
		complement := target - num
		if _, ok := seen[complement]; ok {
			return []int{seen[complement], i}
		}
		seen[num] = i
	}
	return nil
}
