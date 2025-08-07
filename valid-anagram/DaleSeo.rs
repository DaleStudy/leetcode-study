use std::collections::HashMap;

// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut counter: HashMap<char, usize> = HashMap::new();

        for ch in s.chars() {
            *counter.entry(ch).or_insert(0) += 1;
        }

        for ch in t.chars() {
            *counter.entry(ch).or_insert(0) -= 1;
        }

        return counter.values().all(|cnt| *cnt == 0)
    }
}
