// 풀이
// alphabet, number만 걸러내서 소문자로 바꾼 후 reverse한 문자열, 걸러낸 문자열과 비교하여 같은지 확인한다.

// O(n) time complexity
// O(n) space complexity
func isPalindrome(s string) bool {
	regex, _ := regexp.Compile("[a-zA-Z0-9]")

	lowerCaseString := strings.ToLower(s)
	reverseAndFilteredString := ""
	filteredString := ""

	for _, char := range lowerCaseString {
		if regex.MatchString(string(char)) {
			reverseAndFilteredString = c + reverseAndFilteredString
			filteredString += c
		}
	}

	return reverseAndFilteredString == filteredString
}

// O(n) time complexity
// O(n) space complexity
func isPalindrome2(s string) bool {
	lowerCaseString := strings.ToLower(s)
	reverseAndFilteredString := ""
	var filteredString strings.Builder

	for _, char := range lowerCaseString {
		if unicode.IsLetter(char) || unicode.IsDigit(char) {
			reverseAndFilteredString = string(char) + reverseAndFilteredString
			filteredString.WriteRune(char)
		}
	}

	return reverseAndFilteredString == filteredString.String()
}
