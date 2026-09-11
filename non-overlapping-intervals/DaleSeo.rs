// TC: O(n log n)
// SC: O(1)
impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_unstable_by_key(|i| i[1]);
        let mut removed = 0;
        let mut prev_end = i32::MIN;
        for interval in &intervals {
            if interval[0] >= prev_end {
                prev_end = interval[1];
            } else {
                removed += 1;
            }
        }
        removed
    }
}
