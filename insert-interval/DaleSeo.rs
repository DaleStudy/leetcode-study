// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, mut new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::with_capacity(intervals.len() + 1);
        let mut iter = intervals.into_iter().peekable();

        while let Some(interval) = iter.next_if(|i| i[1] < new_interval[0]) {
            result.push(interval);
        }
        while let Some(interval) = iter.next_if(|i| i[0] <= new_interval[1]) {
            new_interval[0] = new_interval[0].min(interval[0]);
            new_interval[1] = new_interval[1].max(interval[1]);
        }
        result.push(new_interval);
        result.extend(iter);

        result
    }
}
