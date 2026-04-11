// TC: O(m * n)
// SC: O(m * n)
func groupAnagrams(strs []string) [][]string {
	groups := map[[26]int][]string{}

	for _, s := range strs {
		var count [26]int
		for _, c := range s {
			count[c-'a']++
		}
		groups[count] = append(groups[count], s)
	}

	result := [][]string{}
	for _, group := range groups {
		result = append(result, group)
	}
	return result
}
