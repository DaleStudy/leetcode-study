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
