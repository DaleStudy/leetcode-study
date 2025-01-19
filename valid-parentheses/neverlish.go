// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import "testing"

func TestIsValid(t *testing.T) {
	result1 := isValid("()")

	if result1 != true {
		t.Errorf("Expected true, but got %v", result1)
	}

	result2 := isValid("()[]{}")
	if result2 != true {
		t.Errorf("Expected true, but got %v", result2)
	}

	result3 := isValid("(]")
	if result3 != false {
		t.Errorf("Expected false, but got %v", result3)
	}

	result4 := isValid("([)]")
	if result4 != false {
		t.Errorf("Expected false, but got %v", result4)
	}
}

func isValid(s string) bool {
	stack := make([]rune, 0)

	for _, c := range s {
		switch c {
		case '(':
			stack = append(stack, ')')
		case '{':
			stack = append(stack, '}')
		case '[':
			stack = append(stack, ']')
		default:
			if len(stack) == 0 || stack[len(stack)-1] != c {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
