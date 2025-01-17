// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import (
	"testing"
)

func TestNumDecodings(t *testing.T) {
	test1 := "12"
	result1 := numDecodings(test1)

	if result1 != 2 {
		t.Errorf("Expected 2, got %d", result1)
	}

	test2 := "226"
	result2 := numDecodings(test2)

	if result2 != 3 {
		t.Errorf("Expected 3, got %d", result2)
	}

	test3 := "0"
	result3 := numDecodings(test3)

	if result3 != 0 {
		t.Errorf("Expected 0, got %d", result3)
	}

	test4 := "06"
	result4 := numDecodings(test4)

	if result4 != 0 {
		t.Errorf("Expected 0, got %d", result4)
	}
}

func numDecodings(s string) int {
	dp := make([]int, len(s)+1)

	dp[0] = 1

	for i := 1; i <= len(s); i++ {
		curBefore1 := s[i-1]
		if curBefore1 != '0' {
			dp[i] += dp[i-1]
		}
		if i > 1 {
			curBefore2 := s[i-2]
			if curBefore2 != '0' && (curBefore2-'0')*10+(curBefore1-'0') <= 26 {
				dp[i] += dp[i-2]
			}
		}
	}

	return dp[len(s)]
}
