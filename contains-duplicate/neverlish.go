package main

import "testing"

func Test(t *testing.T) {
	result1 := containsDuplicate([]int{1, 2, 3, 1})

	if result1 != true {
		t.Fatal("failed test1")
	}

	result2 := containsDuplicate([]int{1, 2, 3, 4})

	if result2 != false {
		t.Fatal("failed test2")
	}
}

func containsDuplicate(nums []int) bool {
	data := make(map[int]bool)

	for _, num := range nums {
		if data[num] {
			return true
		} else {
			data[num] = true
		}
	}
	return false
}
