// TC : O(n) : it iterates for the length of nums
// SC : O(n) : we make hashmap as the size of the given string
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    letterCounts := make(map[rune]int)

    for _, ch := range s {
        letterCounts[ch]++
    }

    for _, ch := range t {
        letterCounts[ch]--
        if letterCounts[ch] < 0 {
            return false
        }
    }

    return true
}
