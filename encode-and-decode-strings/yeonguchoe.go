type Codec struct {
}

// Encodes a list of strings to a single string.
func (codec *Codec) Encode(strs []string) string {
	var temp []rune
	for _, v := range strs {
		var current_string = []rune(v)
		temp = append(temp, rune(len(current_string)))
		temp = append(temp, rune('π'))
		temp = append(temp, current_string...)
	}
	return string(temp)
}

// Decodes a single string to a list of strings.
func (codec *Codec) Decode(strs string) []string {
	var full_string = []rune(strs)
	var result []string

	var index = 0

	for index < len(full_string) {
		var word_start int = int(index)
		for full_string[word_start] != rune('π') {
			word_start += 1
		}
		length := int(full_string[word_start-1])
		result = append(result, string(full_string[word_start+1:word_start+1+length]))
		index = word_start + 1 + length
	}
	return result
}
