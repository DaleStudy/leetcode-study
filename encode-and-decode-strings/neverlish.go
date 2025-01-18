// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import (
	"bytes"
	"fmt"
	"strconv"
	"testing"
)

func TestEncodeAndDecode(t *testing.T) {
	strs := []string{"abc", "def", "ghi"}
	encoded := encode(strs)
	decoded := decode(encoded)
	if len(strs) != len(decoded) {
		t.Errorf("Expected %v but got %v", strs, decoded)
	}
	for i := 0; i < len(strs); i++ {
		if strs[i] != decoded[i] {
			t.Errorf("Expected %v but got %v", strs, decoded)
		}
	}
}

func encode(strs []string) string {
	var buffer bytes.Buffer
	for _, str := range strs {
		buffer.WriteString(fmt.Sprintf("%d~", len(str)))
		buffer.WriteString(str)
	}
	return buffer.String()
}

func decode(str string) []string {
	var result []string
	for i := 0; i < len(str); {
		j := i
		for str[j] != '~' {
			j++
		}
		length, _ := strconv.Atoi(str[i:j])
		result = append(result, str[j+1:j+1+length])
		i = j + 1 + length
	}
	return result
}
