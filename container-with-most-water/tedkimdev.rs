// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let (mut left, mut right) = (0, heights.len() - 1);
        let mut res = 0i32;
        while left <= right {
            res = res.max(((right - left) as i32) * heights[left].min(heights[right]));

            if heights[right] < heights[left] {
                right -= 1;
            } else {
                left += 1;
            }
        }

        res
    }
}
