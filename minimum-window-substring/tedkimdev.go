// TC: O(n * m)
// SC: O(n + m)

func minWindow(s string, t string) string {
	if len(t) > len(s) {
		return ""
	}

	countT := map[byte]int{}
	for i := 0; i < len(t); i++ {
		countT[t[i]]++
	}

	windowMap := map[byte]int{}
	have, need := 0, len(countT)

	left := 0
	resLeft, resRight := -1, -1
	resLen := len(s) + 1

	for right := 0; right < len(s); right++ {
		c := s[right]
		windowMap[c]++

		// update have
		if count, ok := countT[c]; ok {
			if windowMap[c] == count {
				have++
			}
		}

		// window valid -> move left to find minimum
		for have == need {
			if right-left+1 < resLen {
				resLen = right - left + 1
				resLeft, resRight = left, right
			}

			// remove left char
			lc := s[left]
			if count, ok := countT[lc]; ok {
				if windowMap[lc] == count {
					have--
				}
			}
			windowMap[lc]--
			left++
		}
	}

	if resLeft == -1 {
		return ""
	}
	return s[resLeft : resRight+1]
}
