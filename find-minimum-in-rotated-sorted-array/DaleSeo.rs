// TC: O(log n)
// SC: O(1)
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let (mut lo, mut hi) = (0, nums.len() - 1);
        while lo < hi {
            if nums[lo] < nums[hi] {
                return nums[lo];
            }
            let mid = (lo + hi) / 2;
            if nums[mid] > nums[hi] {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        nums[lo]
    }
}
