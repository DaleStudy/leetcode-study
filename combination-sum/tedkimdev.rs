// SC: O(2^t/m)
// TC: O(t/m)
impl Solution {
    pub fn combination_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
		let mut res: Vec<Vec<i32>> = vec![];

		fn dfs(nums: &[i32], target: i32, i: usize, cur: &mut Vec<i32>, mut sum: i32, res: &mut Vec<Vec<i32>>) {
			if sum == target {
				res.push(cur.clone());
				return;
			}
			if i >= nums.len() || sum > target {
				return;
			}

			sum += nums[i];
			cur.push(nums[i]);
			dfs(nums, target, i, cur, sum, res);

			sum -= nums[i];
			cur.pop();
			dfs(nums, target, i+1, cur, sum, res);
		}

		dfs(&nums, target, 0, &mut vec![], 0, &mut res);

		res
    }
}
