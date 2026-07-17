// TC: O(k)
// SC: O(1)
impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let mut n = n as u32;
        let mut cnt = 0;
        while n != 0 {
            n &= n - 1;
            cnt += 1;
        }
        cnt
    }
}
