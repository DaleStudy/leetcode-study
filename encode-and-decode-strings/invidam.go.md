# Intuition
구분자를 넣어 오류를 방지한다.
# Approach
<!-- Describe your approach to solving the problem. -->
1. UTF-8에 벗어나는 구분자 `ㄱ`을 넣어 구분했다.
# Complexity
- Time complexity: $$O(n)$$ 
  - 문자열의 길이 n에 대하여, 이를 순회하는 비용이 발생한다.

- Space complexity: $$O(n)$$
  - 문자열의 길이 n에 대하여, `encoded`를 만드는 공간이 발생한다.

# Code
```go
func encodeV1(strs []string) string {
	ret := strings.Join(strs, string(DIVIDE_CHAR_V1))
	return ret
}

func decodeV1(encoded string) []string {
	sep := string(DIVIDE_CHAR_V1)
	return strings.Split(encoded, sep)
}
```
- - -
# Intuition
솔루션에서 네트워크 통신을 위한다는 목적을 듣고 수정해보았다. (유니코드를 넣는 게 의도는 아닌 듯했다.)
# Approach
1. 구분자 (`-`)와 이전 문자의 길이를 함께 저장한다.
2. 구분자가 나온다면, 문자열의 길이를 추출하여 문자열을 디코딩한다.
3. 위 과정을 배열을 순회하며 반복한다.
# Complexity
- Time complexity: $$O(n)$$
  - 문자열의 길이 n에 대하여, 이를 순회하는 비용이 발생한다.

- Space complexity: $$O(n)$$
  - 문자열의 길이 n에 대하여, `encoded`를 만드는 공간이 발생한다.

# Code
```go
func encode(strs []string) string {
	ret := ""
	for _, str := range strs {
		ret += str
		ret += fmt.Sprintf("%c%04d", DIVIDE_CHAR, len(str))
		// a-1bcd-3
	}
	return ret
}

func decode(encoded string) []string {
	ret := make([]string, 0)
	for i := 0; i < len(encoded); {
		if encoded[i] == DIVIDE_CHAR {
			lenStr := encoded[i+1 : i+5]
			len, _ := strconv.Atoi(lenStr)

			decodeStr := encoded[i-len : i]
			ret = append(ret, decodeStr)
			i += 5
		} else {
			i += 1
		}
	}

	return ret
}
```