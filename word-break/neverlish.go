// 시간복잡도: O(n^2)
// 공간복잡도: O(n)

package main

import "testing"

func TestWordBreak(t *testing.T) {

	result1 := wordBreak("leetcode", []string{"leet", "code"})
	if result1 != true {
		t.Error("Test case 0 failed")
	}

	result2 := wordBreak("applepenapple", []string{"apple", "pen"})
	if result2 != true {
		t.Error("Test case 1 failed")
	}

	result3 := wordBreak("catsandog", []string{"cats", "dog", "sand", "and", "cat"})
	if result3 != false {
		t.Error("Test case 2 failed")
	}
}

func wordBreak(s string, wordDict []string) bool {
	wordMap := make(map[string]bool)

	for _, word := range wordDict {
		wordMap[word] = true
	}

	dp := make([]bool, len(s)+1)
	dp[0] = true
	for i := 1; i <= len(s); i++ {
		for j := 0; j < i; j++ {
			word := s[j:i]
			if dp[j] && wordMap[word] {
				dp[i] = true
				break
			}
		}
	}

	return dp[len(s)]
}
