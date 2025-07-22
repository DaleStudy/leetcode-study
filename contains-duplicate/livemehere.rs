use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set: HashSet<i32> = HashSet::new();
        for &n in nums.iter() {
            if set.contains(&n) {
                return true;
            }
            set.insert(n);
        }
        false
    }
}
