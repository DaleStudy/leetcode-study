use std::collections::HashMap;

// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut indices = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&j) = indices.get(&complement) {
                return vec![j as i32, i as i32];
            }
            indices.insert(num, i);
        }
        vec![]
    }
}
