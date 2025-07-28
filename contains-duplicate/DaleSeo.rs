use std::collections::HashSet;

// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();
        !nums.into_iter().all(|num| set.insert(num))
    }
}
