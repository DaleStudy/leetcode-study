use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for (idx, &n) in nums.iter().enumerate() {
            let pair = target - n;
            if let Some(&pair_idx) = map.get(&pair) {
                return vec![idx as i32, pair_idx];
            } else {
                map.insert(n, idx as i32);
            }
        }
        vec![]
    }
}
