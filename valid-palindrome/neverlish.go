// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import (
	"strings"
	"testing"
)

func Test(t *testing.T) {
	result1 := isPalindrome("A man, a plan, a canal: Panama")
	if result1 != true {
		t.Fatal("failed test1")
	}

	result2 := isPalindrome("race a car")
	if result2 != false {
		t.Fatal("failed test2")
	}

	result3 := isPalindrome("")

	if result3 != true {
		t.Fatal("failed test3")
	}
}

func isPalindrome(s string) bool {
	s = strings.ToLower(s)

	var filtered []rune
	for _, r := range s {
		if ('a' <= r && r <= 'z') || ('0' <= r && r <= '9') {
			filtered = append(filtered, r)
		}
	}

	for index, r := range filtered[:len(filtered)/2] {
		if r != filtered[len(filtered)-index-1] {
			return false
		}
	}
	return true
}
