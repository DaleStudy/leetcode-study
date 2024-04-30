func isPalindrome(s string) bool {
	filtered := strings.Map(func(r rune) rune {
		if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
			return -1
		}
		return unicode.ToLower(r)
	}, s)

	for ldx, rdx := 0, len(filtered) - 1; ldx < rdx; ldx, rdx = ldx + 1, rdx - 1 {
		if filtered[ldx] != filtered[rdx] {
			return false
		}
	}
	return true
}
