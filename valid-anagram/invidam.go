func isAnagram(s string, t string) bool {
	freqS := make(map[rune]int, 26)
	freqT := make(map[rune]int, 26)

	for _, ch := range s {
		if _, ok := freqS[ch]; ok {
			freqS[ch]++
		} else {
			freqS[ch] = 1
		}
	}
	for _, ch := range t {
		freqT[ch]++
	}

	for ch := 'a'; ch <= 'z'; ch++ {
		if diff := freqS[ch] - freqT[ch]; diff != 0 {
			return false
		}
	}

	return true
}
