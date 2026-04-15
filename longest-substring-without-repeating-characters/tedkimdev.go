// TC: O(n)
// SC: O(m)
func lengthOfLongestSubstring(s string) int {
	charIndex := map[byte]int{}

	maxLen := 0
	left := 0
	for right := 0; right < len(s); right++ {
		if idx, ok := charIndex[s[right]]; ok && idx >= left {
			left = idx + 1
		}
		charIndex[s[right]] = right
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}

	return maxLen
}
