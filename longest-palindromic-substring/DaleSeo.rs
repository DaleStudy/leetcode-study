// TC: O(n^2)
// SC: O(1)
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let bytes = s.as_bytes();
        let mut best = 0..0;

        for center in 0..bytes.len() {
            for end in center..=center + 1 {
                let (mut left, mut right) = (center, end);
                while left > 0 && right < bytes.len() && bytes[left - 1] == bytes[right] {
                    left -= 1;
                    right += 1;
                }
                if right - left > best.len() {
                    best = left..right;
                }
            }
        }

        s[best].to_owned()
    }
}
