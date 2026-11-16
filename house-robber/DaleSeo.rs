// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut prev, mut curr) = (0, 0);
        for num in nums {
            (prev, curr) = (curr, curr.max(num + prev));
        }
        curr
    }
}
