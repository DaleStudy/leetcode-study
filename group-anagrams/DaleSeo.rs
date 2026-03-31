// TC: O(n * k) where n = number of strings, k = max string length
// SC: O(n * k)
use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut anagrams: HashMap<[u8; 26], Vec<String>> = HashMap::new();
        for s in strs {
            let mut count = [0u8; 26];
            for b in s.bytes() {
                count[(b - b'a') as usize] += 1;
            }
            anagrams.entry(count).or_default().push(s);
        }
        anagrams.into_values().collect()
    }
}
