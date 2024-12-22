// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import (
	"testing"
)

func Test(t *testing.T) {
	result1 := isAnagram("anagram", "nagaram")

	if !result1 {
		t.Fatal("failed test1")
	}

	result2 := isAnagram("rat", "car")

	if result2 {
		t.Fatal("failed test2")
	}
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sMap := make(map[rune]int)

	for _, c := range s {
		sMap[c]++
	}

	for _, c := range t {
		if _, ok := sMap[c]; !ok {
			return false
		}

		sMap[c]--

		if sMap[c] == 0 {
			delete(sMap, c)
		}
	}

	return len(sMap) == 0
}
