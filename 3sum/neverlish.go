// 시간복잡도: O(n^2)
// 공간복잡도: O(n)

package main

import (
	"sort"
	"testing"
)

func TestThreeSum(t *testing.T) {
	test1 := []int{-1, 0, 1, 2, -1, -4}
	result1 := threeSum(test1)
	
	for _, comp := range result1 {
		for _, num := range comp {
			t.Logf("%d ", num)
		}
	}

	println("YO")

	if len(result1) != 2 {
		t.Errorf("Expected 2, got %d", len(result1))
	}
}

func twoSum(nums []int, target int) [][]int {
	result := [][]int{}
	seen := map[int]int{}
	for i, num := range nums {
		complement := target - num
		if _, ok := seen[complement]; ok {
			result = append(result, []int{seen[complement], i})
		}
		seen[num] = i
	}

	return result
}

func threeSum(nums []int) [][]int {
	result := map[int]map[int]map[int]bool{}

	for i, num := range nums[:len(nums)-2] {
		if (i > 0 && num == nums[i-1]) {
			continue
		}
		for _, comp := range twoSum(nums[i+1:], 0-num) {
			comps := []int{num, nums[comp[0]+i+1], nums[comp[1]+i+1]}
			sort.Ints(comps)
			comp1 := comps[0]
			comp2 := comps[1]
			comp3 := comps[2]
			if _, ok := result[comp1]; !ok {
				result[comp1] = map[int]map[int]bool{}
			}
			if _, ok := result[comp1][comp2]; !ok {
				result[comp1][comp2] = map[int]bool{}
			}
			result[comp1][comp2][comp3] = true
		}
	}
		
	

	answers := [][]int{}
	for key1 := range result {
		
		for key2 := range result[key1] {
			for key3 := range result[key1][key2] {
				comp := []int{key1, key2, key3}
				answers = append(answers, comp)
			}
		}
	}

	return answers
}
