// 시간복잡도: O(n^2)
// 공간복잡도: O(n)

package main

import "testing"

func TestLengthOfLongestSubstring(t *testing.T) {
	result1 := lengthOfLongestSubstring("abcabcbb")

	if result1 != 3 {
		t.Errorf("Expected 3, but got %v", result1)
	}

	result2 := lengthOfLongestSubstring("bbbbb")
	if result2 != 1 {
		t.Errorf("Expected 1, but got %v", result2)
	}

	result3 := lengthOfLongestSubstring("pwwkew")
	if result3 != 3 {
		t.Errorf("Expected 3, but got %v", result3)
	}

	result4 := lengthOfLongestSubstring("")
	if result4 != 0 {
		t.Errorf("Expected 0, but got %v", result4)
	}
}

func lengthOfLongestSubstring(s string) int {
	result := 0

	for i := 0; i < len(s); i++ {
		m := make(map[rune]bool)
		for j := i; j < len(s); j++ {
			if _, ok := m[rune(s[j])]; ok {
				break
			}
			m[rune(s[j])] = true
		}

		if len(m) > result {
			result = len(m)
		}
	}

	return result
}
