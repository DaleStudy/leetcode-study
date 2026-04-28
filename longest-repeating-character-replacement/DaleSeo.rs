// TC: O(n), where n is s.len()
// SC: O(1), fixed 26-slot frequency array
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let mut counts = [0i32; 26];
        let mut start = 0usize;
        let mut max_freq = 0i32;
        let mut result = 0i32;

        for end in 0..bytes.len() {
            let idx = (bytes[end] - b'A') as usize;
            counts[idx] += 1;
            max_freq = max_freq.max(counts[idx]);

            while (end - start + 1) as i32 - max_freq > k {
                let left_idx = (bytes[start] - b'A') as usize;
                counts[left_idx] -= 1;
                start += 1;
            }

            result = result.max((end - start + 1) as i32);
        }

        result
    }
}
