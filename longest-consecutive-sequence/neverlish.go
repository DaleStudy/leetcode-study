// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import "testing"

func Test(t *testing.T) {
	result := longestConsecutive([]int{100, 4, 200, 1, 3, 2})

	if result != 4 {
		t.Fatal("failed test")
	}

	result2 := longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1})

	if result2 != 9 {
		t.Fatal("failed test2")
	}
}

func longestConsecutive(nums []int) int {
	numsSet := make(map[int]bool)

	for _, num := range nums {
		numsSet[num] = true
	}

	longest := 0

	for num := range numsSet {
		if !numsSet[num-1] {
			currentNum := num
			currentLength := 1

			for numsSet[currentNum+1] {
				currentNum++
				currentLength++
			}

			if currentLength > longest {
				longest = currentLength
			}
		}
	}

	return longest
}
