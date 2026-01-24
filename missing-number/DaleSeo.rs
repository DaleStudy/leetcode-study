// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut xor = nums.len() as i32;
        for (i, &num) in nums.iter().enumerate() {
            xor ^= i as i32 ^ num;
        }
        xor
    }
}
