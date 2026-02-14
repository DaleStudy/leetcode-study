// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut ans = vec![0i32; n + 1];
        for i in 1..=n {
            ans[i] = ans[i >> 1] + (i & 1) as i32;
        }
        ans
    }
}
