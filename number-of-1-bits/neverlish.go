// 시간복잡도: O(1)
// 공간복잡도: O(1)

package main

import "testing"

func Test_hammingWeight(t *testing.T) {
	result1 := hammingWeight(11)
	if result1 != 3 {
		t.Fatal(result1)
	}

	result2 := hammingWeight(128)

	if result2 != 1 {
		t.Fatal(result2)
	}

	result3 := hammingWeight(2147483645)

	if result3 != 30 {
		t.Fatal(result3)
	}
}

func hammingWeight(n int) int {
	result := 0
	for n > 0 {
		result += n & 1
		n >>= 1
	}
	return result
}
