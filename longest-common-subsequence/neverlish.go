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
	commonSubsequence := make([][]int, len(text1)+1)

	for i := 0; i < len(text1)+1; i++ {
		commonSubsequence[i] = make([]int, len(text2)+1)
	}

	for i := 1; i < len(text1)+1; i++ {
		for j := 1; j < len(text2)+1; j++ {
			if text1[i-1] == text2[j-1] {
				commonSubsequence[i][j] = commonSubsequence[i-1][j-1] + 1
			} else {
				commonSubsequence[i][j] = max(commonSubsequence[i-1][j], commonSubsequence[i][j-1])
			}
		}
	}

	return commonSubsequence[len(text1)][len(text2)]
}
