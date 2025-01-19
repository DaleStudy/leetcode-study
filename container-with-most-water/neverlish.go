package main

import "testing"

func TestMaxArea(t *testing.T) {
	result1 := maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7})

	if result1 != 49 {
		t.Errorf("Expected 49, but got %v", result1)
	}

	result2 := maxArea([]int{1, 1})

	if result2 != 1 {
		t.Errorf("Expected 1, but got %v", result2)
	}
}

func maxArea(height []int) int {
	result := 0

	pointer_left := 0
	pointer_right := len(height) - 1

	for pointer_left < pointer_right {
		area := (pointer_right - pointer_left) * min(height[pointer_left], height[pointer_right])
		result = max(result, area)

		if height[pointer_left] < height[pointer_right] {
			pointer_left++
		} else {
			pointer_right--
		}
	}

	return result
}
