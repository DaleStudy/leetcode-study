package main

import (
	"testing"
)

func Test(t *testing.T) {
	result1 := rob([]int{1, 2, 3, 1})

	if result1 != 4 {
		t.Fatal("failed test1")
	}

	result2 := rob([]int{2, 7, 9, 3, 1})

	if result2 != 12 {
		t.Fatal("failed test2")
	}
}

func rob(nums []int) int {
	length := len(nums)

	if length == 0 {
		return 0
	}
	if length == 1 {
		return nums[0]
	}

	moneys := make([]int, length)

	moneys[0] = nums[0]
	moneys[1] = max(nums[0], nums[1])

	for position := 2; position < length; position++ {
		moneys[position] = max(moneys[position-1], moneys[position-2]+nums[position])
	}

	return moneys[length-1]
}
