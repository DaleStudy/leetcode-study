use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut set: HashSet<i32> = HashSet::new();
        let mut max_seq: i32 = 0;

        for &n in nums.iter() {
            set.insert(n);
        }

        for &n in set.iter() {
            // 시작점
            if !set.contains(&(n - 1)) {
                let mut j = n + 1;
                while set.contains(&j) {
                    j += 1;
                }

                let seq = j - n;
                if seq > max_seq {
                    max_seq = seq
                }
            }
        }

        return max_seq;
    }
}
