func isAnagram(s string, t string) bool {

	var s_frequency map[rune]int = make(map[rune]int)
	var t_frequency map[rune]int = make(map[rune]int)

	for i := 0; i < len(s); i++ {
		s_frequency[rune(s[i])] += 1
	}

	for index, key := range t {
		t_frequency[key] += 1
	}

	for key, value := range s_frequency {
		if v, key_exist := t_frequency[key]; !key_exist || v != value {
			return false
		}
	}

	for key, value := range t_frequency {
		if v, key_exist := s_frequency[key]; !key_exist || v != value {
			return false
		}
	}

	return true
}
