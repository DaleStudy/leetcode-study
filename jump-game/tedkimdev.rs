// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
		let mut last = nums.len() as i32 - 1;
		
		for i in (0..nums.len() as i32 - 1).rev() {
			if i + nums[i as usize] >= last {
				last = i;
			}
		}
		last == 0
    }
}
