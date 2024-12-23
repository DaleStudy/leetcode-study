// 시간복잡도 : O(n)
// 공간복잡도 : O(1)

package main

import "testing"

func TestProductExceptSelf(t *testing.T) {
	test1 := productExceptSelf([]int{1, 2, 3, 4})
	if len(test1) != 4 {
		t.Errorf("Expected 4, got %d", len(test1))
	}

	if test1[0] != 24 && test1[1] != 12 && test1[2] != 8 && test1[3] != 6 {
		t.Errorf("Expected [24, 12, 8, 6], got %v", test1)
	}

	test2 := productExceptSelf([]int{0, 0})

	if len(test2) != 2 {
		t.Errorf("Expected 2, got %d", len(test2))
	}

	if test2[0] != 0 && test2[1] != 0 {
		t.Errorf("Expected [0, 0], got %v", test2)
	}

	test3 := productExceptSelf([]int{-1,1,0,-3,3})
	if len(test3) != 5 {
		t.Errorf("Expected 5, got %d", len(test3))
	}

	if test3[0] != 0 && test3[1] != 0 && test3[2] != 9 && test3[3] != 0 && test3[4] != 0 {
		t.Errorf("Expected [0, 0, 9, 0, 0], got %v", test3)
	}
}

func productExceptSelf(nums []int) []int {
	zeroCount := 0
	product := 1

	for _, num := range nums {
		if num == 0 {
			zeroCount++
		} else {
			product *= num
		}
	}

	result := make([]int, len(nums))

	if zeroCount > 1 {
		return result
	}

	for i, num := range nums {
		if zeroCount == 1 {
			if num == 0 {
				result[i] = product
			} else {
				result[i] = 0
			}
		} else {
			result[i] = product / num
		}
	}

	return result
}
