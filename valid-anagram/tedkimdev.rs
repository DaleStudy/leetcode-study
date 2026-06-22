// TC: O(n) - n is the length of the strings
// SC: O(1) - lowercase english letters
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
		if s.len() != t.len() {
			return false;
		}

		let mut count_map: HashMap<u8, i32> = HashMap::new();

		for (a, b) in s.bytes().zip(t.bytes()) {
			*count_map.entry(a).or_insert(0) += 1;
			*count_map.entry(b).or_insert(0) -= 1;
		}

		count_map.values().all(|&v| v == 0)
    }
}
