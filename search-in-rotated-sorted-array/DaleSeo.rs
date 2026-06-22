// TC: O(log n)
// SC: O(1)
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut low = 0i32;
        let mut high = nums.len() as i32 - 1;

        while low <= high {
            let mid = low + (high - low) / 2;
            let mid_val = nums[mid as usize];

            if mid_val == target {
                return mid;
            }

            if nums[low as usize] <= mid_val {
                if nums[low as usize] <= target && target < mid_val {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if mid_val < target && target <= nums[high as usize] {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        -1
    }
}
