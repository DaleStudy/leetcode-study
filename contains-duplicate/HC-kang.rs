impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut set = HashSet::new();
        for num in nums {
            if !set.insert(num) {
                return true;
            }
        }
        false
    }
}
