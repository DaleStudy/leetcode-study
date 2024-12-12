// 풀이
// 유효한 string 값만 정제하고 palindrome check.

// TC
// 입력된 string의 길이에 따라 최대 O(n)

// SC
// validStr으로 유효한 string을 정제하기 때문에 최대 O(n)

// (+) 입력된 string을 사용하는 방식으로 개선하면 SC가 O(1)

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	validStr := ""
	for _, str := range s {
		if ('a' > str || 'z' < str) && ('0' > str || '9' < str) {
			continue
		}
		validStr += string(str)
	}
	if len(validStr) <= 1 {
		return true
	}
	l := len(validStr)
	for i := 0; i < l/2; i++ {
		if validStr[i] != validStr[l-1-i] {
			return false
		}
	}
	return true
}
