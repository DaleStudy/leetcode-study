// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return nums[0];
        }
        Self::rob_line(&nums[..n - 1]).max(Self::rob_line(&nums[1..]))
    }

    fn rob_line(houses: &[i32]) -> i32 {
        houses
            .iter()
            .fold((0, 0), |(prev, curr), &money| (curr, curr.max(prev + money)))
            .1
    }
}
