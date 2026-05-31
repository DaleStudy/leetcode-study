// TC: O(n logn)
// SC: O(1)
impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {
        intervals.sort_by_key(|i| i[0]);
        intervals.windows(2).all(|w| w[0][1] <= w[1][0])
    }
}
