// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut xor_result = n;
        for i in 0..nums.len() {
            xor_result ^= i as i32 ^ nums[i];
        }
        xor_result
    }
}
