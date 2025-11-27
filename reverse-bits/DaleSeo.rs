// TC: O(1)
// SC: O(1)
impl Solution {
    pub fn reverse_bits(n: i32) -> i32 {
        let mut result = 0u32;
        let mut num = n as u32;

        for i in 0..32 {
            // Extract the least significant bit
            let bit = num & 1;
            // Place it in the reversed position
            result |= bit << (31 - i);
            // Shift num right to process the next bit
            num >>= 1;
        }

        result as i32
    }
}
