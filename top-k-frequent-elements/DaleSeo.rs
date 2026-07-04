use std::collections::HashMap;

// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freqs = HashMap::new();
        for &num in &nums {
            *freqs.entry(num).or_insert(0) += 1;
        }

        let mut buckets = vec![Vec::new(); nums.len() + 1];
        for (num, freq) in freqs {
            buckets[freq].push(num);
        }

        let mut top_nums = Vec::new();
        for bucket in buckets.into_iter().rev() {
            for num in bucket {
                top_nums.push(num);
                if top_nums.len() == k as usize {
                    return top_nums;
                }
            }
        }

        top_nums
    }
}
