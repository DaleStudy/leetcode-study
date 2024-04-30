func isPalindrome(s string) bool {
	filtered := ""
	for _, ch := range s {
		if unicode.IsLetter(ch) || unicode.IsNumber(ch) {
			filtered += string(unicode.ToLower(ch))
		}
	}

	for ldx, rdx := 0, len(filtered) - 1; ldx < rdx; ldx, rdx = ldx + 1, rdx - 1 {
		if filtered[ldx] != filtered[rdx] {
			return false
		}
	}
	return true
}
