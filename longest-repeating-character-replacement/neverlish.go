// 시간복잡도: O(n)
// 공간복잡도: O(1)

package main

import "testing"

func Test_characterReplacement(t *testing.T) {
	result1 := characterReplacement("ABAB", 2)
	if result1 != 4 {
		t.Fatal(result1)
	}

	result2 := characterReplacement("AABABBA", 1)
	if result2 != 4 {
		t.Fatal(result2)
	}
}

func maxValue(m map[byte]int) int {
	max := 0
	for _, v := range m {
		if v > max {
			max = v
		}
	}
	return max
}

func characterReplacement(s string, k int) int {
	max_length := 0
	counter := make(map[byte]int)

	window_start := 0
	window_end := 0

	for window_end < len(s) {
		counter[s[window_end]]++

		for window_end-window_start+1-maxValue(counter) > k {
			counter[s[window_start]]--
			window_start++
		}

		max_length = max(max_length, window_end-window_start+1)

		window_end++
	}

	return max_length
}
