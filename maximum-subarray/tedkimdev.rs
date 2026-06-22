// SC: O(1)
// TC: O(n)
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_sub = nums[0];
        let mut cur_sum = 0;
        for &num in &nums {
            if cur_sum < 0 {
                cur_sum = 0;
            }
            cur_sum += num;
            max_sub = max_sub.max(cur_sum);
        }
        max_sub
    }
}
