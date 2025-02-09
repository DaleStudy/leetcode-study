// 시간복잡도: O(n^3)
// 공간복잡도: O(n^2)

package main

import "testing"

func expect(input string, expected int, t *testing.T) {
	result := countSubstrings(input)
	if result != expected {
		t.Errorf("Expected %d but got %d", expected, result)
	}
}

func TestCountSubstrings(t *testing.T) {
	expect("abc", 3, t)
	expect("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg", 77, t)
}

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func countSubstrings(s string) int {
	result := 0
	
	for i := 0; i < len(s); i++ {
		for j := i; j < len(s); j++ {
			if isPalindrome(s[i:j+1]) {
				result++
			}
		}
	}
	return result
}
