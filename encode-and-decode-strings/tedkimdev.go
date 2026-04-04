type Solution struct{}

// TC: O(m)
// SC: O(m + n)
func (s *Solution) Encode(strs []string) string {
	encoded := ""
	for _, str := range strs {
		encoded += fmt.Sprintf("%d|%s", len(str), str)
	}

	return encoded
}

// TC: O(m)
// SC: O(m + n)
func (s *Solution) Decode(encoded string) []string {
	decoded := make([]string, 0)

	i := 0
	for i < len(encoded) {
		j := i
		for encoded[j] != '|' {
			j++
		}
		length, _ := strconv.Atoi(encoded[i:j])
		i = j + 1
		decoded = append(decoded, encoded[i:i+length])
		i += length
	}

	return decoded
}
