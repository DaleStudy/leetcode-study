impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut nx = nums;
        nx.sort();

        for i in 1..nx.len() {
            if nx[i] == nx[i - 1] {
                return true;
            }
        }

        false
    }
}
