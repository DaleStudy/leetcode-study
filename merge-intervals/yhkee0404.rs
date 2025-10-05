use itertools::Itertools;
use std::cmp::max;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals: Vec<_> = intervals.iter()
                .cloned()
                .sorted_by(|a, b| a.cmp(b)) // T(n) = O(nlogn)
                .collect();
        let mut ans: Vec<Vec<i32>> = vec![];
        let mut end = -1;
        for interval in intervals {
            if ans.is_empty() || ans.last().unwrap()[1] < interval[0] {
                ans.push(interval) // S(n) = O(n)
            } else {
                ans.last_mut().unwrap()[1] = max(ans.last().unwrap()[1], interval[1])
            }
        }
        ans
    }
}
