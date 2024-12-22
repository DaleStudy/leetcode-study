package valid_anagram

/**
 * 풀이:
 * t가 s의 anagram인지 확인하는 문제!
 * s를 hashmap에 맵핑하고, t의 rune r을 하나씩 s[r] 로 갯수를 체크하여 풀음.
 * anagram이면 return true, otherwise false
 * true 까지 조건 3개가 있음.
 *
 * TC: O(N) -> s나 t의 길이 만큼만 돌음
 * SC: O(N) -> M * N에서 최고차항 정리
 */
func isAnagram(s string, t string) bool {
	ht := make(map[rune]int, len(s))
	for _, r := range s {
		ht[r]++
	}

	for _, r := range t {
		cnt, ok := ht[r]
		if !ok { // 1. t에 존재하지 않는 rune -> false
			return false
		}

		ht[r] -= 1     // t의 rune이 s에 존재하므로 갯수 1 차감
		if cnt-1 < 0 { // 2. s에 있는 rune보다 더 많이 가지고 있음
			return false
		}
	}

	for _, v := range ht {
		if v > 0 { // 3. t를 순회하고 s에 남아있는게 있어도 false
			return false
		}
	}

	return true
}

func isAnagram_faster(s string, t string) bool {
	if len(s) != len(t) { // 둘이 길이가 다르면 당연히 실패함
		return false
	}

	ht := make(map[byte]int, len(s))
	for i, _ := range s {
		ht[s[i]]++
		ht[t[i]]-- // 기존에 푼 방식에서 ok 체크 안해버림? ..
	}

	for _, v := range ht {
		if v != 0 {
			return false
		}
	}
	return true
}
