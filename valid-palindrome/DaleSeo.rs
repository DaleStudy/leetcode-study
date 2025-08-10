// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let bytes = s.as_bytes();
        let (mut low, mut high) = (0, bytes.len() - 1);
        while low < high {
            while low < high && !bytes[low].is_ascii_alphanumeric() {
                low += 1
            }
            while low < high && !bytes[high].is_ascii_alphanumeric() {
                high -= 1
            }
            if low == high {
                return true;
            }
            if bytes[low].to_ascii_lowercase() != bytes[high].to_ascii_lowercase() {
                return false;
            }
            low += 1;
            high -= 1;
        }
        true
    }
}
