package valid_anagram

func isAnagram(s string, t string) bool {
	ht := make(map[rune]int, len(s))
	for _, r := range s {
		ht[r]++
	}

	for _, r := range t {
		cnt, ok := ht[r]
		if !ok {
			return false
		}

		ht[r] -= 1
		if cnt-1 < 0 {
			return false
		}
	}

	for _, v := range ht {
		if v > 0 {
			return false
		}
	}

	return true
}
