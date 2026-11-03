// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn to_lower_case(s: String) -> String {
        s.chars()
            .map(|c| {
                if c.is_ascii_uppercase() {
                    (c as u8 + (b'a' - b'A')) as char
                } else {
                    c
                }
            })
            .collect()
    }
}
