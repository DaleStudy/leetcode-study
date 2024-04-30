func isPalindrome(s string) bool {
	var sb strings.Builder
	sb.Grow(len(s))
	for _, ch := range s {
		if unicode.IsLetter(ch) || unicode.IsNumber(ch) {
			sb.WriteRune(unicode.ToLower(ch))
		}
	}
	filtered := sb.String()
	for ldx, rdx := 0, len(filtered)-1; ldx < rdx; ldx, rdx = ldx+1, rdx-1 {
		if filtered[ldx] != filtered[rdx] {
			return false
		}
	}
	return true
}
