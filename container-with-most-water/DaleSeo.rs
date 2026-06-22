// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut max_area = 0;
        let (mut left, mut right) = (0, height.len() - 1);
        while left < right {
            let width = (right - left) as i32;
            let min_height = height[left].min(height[right]);
            let area = width * min_height;
            max_area = max_area.max(area);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        max_area
    }
}
