// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_total = nums[0];
        let mut total = nums[0];
        for &num in &nums[1..] {
            total = num.max(total + num);
            max_total = max_total.max(total);
        }
        max_total
    }
}
