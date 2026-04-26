// TC: O(1)
// SC: O(1)
impl Solution {
    pub fn reverse_bits(n: u32) -> u32 {
        let mut res: u32 = 0;
        for i in 0..32 {
            let bit = (n >> i) & 1;
            res += bit << (31 - i);
        }
        res
    }
}
