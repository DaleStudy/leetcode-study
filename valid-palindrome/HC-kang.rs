/**
 * https://leetcode.com/problems/valid-palindrome
 * T.C. O(n)
 * S.C. O(n)
 */
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s: Vec<char> = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect(); // T.C. O(n), S.C. O(n)
            
        let mut i = 0;
        let mut j = s.len().saturating_sub(1);
        
        // T.C. O(n)
        while i < j {
            if s[i] != s[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}

/**
 * 최적화
 * T.C. O(n)
 * S.C. O(1)
 */
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s.as_bytes();
        let (mut left, mut right) = (0, s.len().saturating_sub(1));

        while (left < right) {
            while (left < right && !Self::is_alphanumeric(s[left])) {
                left += 1;
            }

            while (left < right && !Self::is_alphanumeric(s[right])) {
                right -= 1;
            }

            if left < right {
                if s[left].to_ascii_lowercase() != s[right].to_ascii_lowercase() {
                    return false;
                }
                left += 1;
                right -= 1;
            }
        }

        true
    }

    fn is_alphanumeric(c: u8) -> bool {
        (c >= b'a' && c <= b'z') ||
        (c >= b'A' && c <= b'Z') ||
        (c >= b'0' && c <= b'9')
    }
}
