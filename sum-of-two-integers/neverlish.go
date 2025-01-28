// 시간복잡도: O(1)
// 공간복잡도: O(1)

package main

import "testing"

func Test_getSum(t *testing.T) {
	result1 := getSum(1, 2)
	if result1 != 3 {
		t.Fatal(result1)
	}

	result2 := getSum(2, 3)
	if result2 != 5 {
		t.Fatal(result2)
	}
}

func getSum(a int, b int) int {
	for b != 0 {
		carry := a & b
		a = a ^ b
		b = carry << 1
	}
	return a
}
