// 풀이
// s의 rune을 key로 같은 철자의 갯수를 담게하고
// t와 비교하면서 갯수를 하나씩 감소하게 해서
// 남은 철자가 있거나 (s에는 있고, r에는 없는 철자가 있는 경우)
// 더 감소된 철자가 있으면 (s에는 없고, r에만 있는 철자가 있는 경우) false가 return 되게 함.

// TC
// O(n+n+n) = O(n)

// SC
// s의 길이만큼 늘어나는 map으로 인해 O(n)

func isAnagram(s string, t string) bool {
	m := make(map[rune]int)
	for _, r := range s {
		m[r]++
	}
	for _, r := range t {
		m[r]--
	}
	for _, count := range m {
		if count < 0 || count > 0 {
			return false
		}
	}
	return true
}
