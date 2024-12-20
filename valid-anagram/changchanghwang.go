// Time complexity, O(n)
// Space complexity, O(1)
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	count := make([]int, 26)

	for index, _ := range count {
		count[index] = 0
	}

	for i := 0; i < len(s); i++ {
		count[int(s[i])-int('a')]++ // s의 문자를 카운트하고
		count[int(t[i])-int('a')]-- // a의 문자를 -1 한다.
	}

	for _, val := range count {
		if val != 0 { // 0이 아니라면 다른 문자열이 있는것이기 때문에 false
			return false
		}
	}
	return true
}
