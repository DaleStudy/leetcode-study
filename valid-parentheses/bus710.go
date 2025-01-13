package hello

import (
	"strings"
)

const (
	openChar  = "({["
	closeChar = ")]}"
)

func isValid(s string) bool {
	ss := strings.Split(s, "")
	stack := []string{}

	// If the very first one is not an opening character,
	// no need to check followings
	if !strings.Contains(openChar, ss[0]) || !strings.Contains(closeChar, ss[len(ss)-1]) {
		return false
	}

	// If the length is not even, there is an incomplete pair
	if len(ss)%2 == 1 {
		return false
	}

	// Loop over the slice to check
	// - If the current one is an opening one, then push into the stack
	// - If the current one is a closing one, then pop and compare with the previous one from the stack
	for _, c := range ss {
		if strings.Contains(openChar, c) {
			stack = append(stack, c)
		} else if strings.Contains(closeChar, c) {
			if len(stack) == 0 {
				return false
			}
			prev := stack[len(stack)-1]

			switch {
			case prev == "(" && c == ")":
				fallthrough
			case prev == "[" && c == "]":
				fallthrough
			case prev == "{" && c == "}":
				stack = stack[:len(stack)-1]
			default:
				stack = append(stack, c)
			}
		} else {
			// In case of non-parenthesis character found
			return false
		}
	}
	return len(stack) == 0
}
