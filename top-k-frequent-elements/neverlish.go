package main

import "testing"

func Test(t *testing.T) {
	result := topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2)

	if result[0] != 1 || result[1] != 2 {
		t.Fatal("failed test")
	}
}

func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int)

	for _, num := range nums {
		freq[num]++
	}

	freq_by_counts := make(map[int][]int)

	for num, count := range freq {
		if _, ok := freq_by_counts[count]; !ok {
			freq_by_counts[count] = []int{}
		}
		freq_by_counts[count] = append(freq_by_counts[count], num)
	}

	result := make([]int, 0, k)

	for count := len(nums); count > 0; count-- {
		if nums, ok := freq_by_counts[count]; ok {
			if len(result) >= k {
				break
			}
			result = append(result, nums...)
		}
	}
	return result
}
