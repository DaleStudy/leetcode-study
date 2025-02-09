// 시간복잡도: O(n^2)
// 공간복잡도: O(n^2)

package main

import "testing"

func Test_longestCommonSubsequence(t *testing.T) {
	result1 := longestCommonSubsequence("abcde", "ace")

	if result1 != 3 {
		t.Fatal(result1)
	}

	result2 := longestCommonSubsequence("abc", "abc")

	if result2 != 3 {
		t.Fatal(result2)
	}

	result3 := longestCommonSubsequence("abc", "def")

	if result3 != 0 {
		t.Fatal(result3)
	}
}

func longestCommonSubsequence(text1 string, text2 string) int {
	prev := make([]int, len(text2)+1)
	curr := make([]int, len(text2)+1)

	for i := 1; i <= len(text1); i++ {
		for j := 1; j <= len(text2); j++ {
			if text1[i-1] == text2[j-1] {
				curr[j] = prev[j-1] + 1
			} else {
				curr[j] = max(prev[j], curr[j-1])
			}
		}
		prev, curr = curr, prev
	}

	return prev[len(text2)]
}
