// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import "testing"

func TestGroupAnagrams(t *testing.T) {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	result := groupAnagrams(strs)

	if len(result) != 3 {
		t.Error("Test case 0 failed")
	}

	if len(result[0]) != 3 {
		t.Error("Test case 1 failed")
	}

	if len(result[1]) != 3 {
		t.Error("Test case 2 failed")
	}

	if len(result[2]) != 1 {
		t.Error("Test case 3 failed")
	}
}

func groupAnagrams(strs []string) [][]string {
	result := make([][]string, 0)

	m := make(map[[26]int]int)

	for _, str := range strs {
		key := [26]int{}
		for _, c := range str {
			key[c-'a']++
		}

		if idx, ok := m[key]; ok {
			result[idx] = append(result[idx], str)
		} else {
			m[key] = len(result)
			result = append(result, []string{str})
		}
	}

	return result
}
