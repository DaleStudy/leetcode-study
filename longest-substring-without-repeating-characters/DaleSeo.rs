// TC: O(n)
// SC: O(1)
use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_len = 0;
        let mut chars = HashMap::new();
        let mut start = 0;

        for (end, ch) in s.chars().enumerate() {
            if let Some(&prev) = chars.get(&ch) {
                if prev >= start {
                    start = prev + 1;
                }
            }
            chars.insert(ch, end);
            max_len = max_len.max(end - start + 1);
        }

        max_len as i32
    }
}
