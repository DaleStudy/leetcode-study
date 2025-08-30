impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        return Self::solve(&nums, 0, nums.len()).unwrap_or(0);
    }
    fn solve(nums: &Vec<i32>, l: usize, r: usize) -> Option<i32> {
        if l >= r {
            return None
        }
        if l + 1 == r {
            return Some(nums[l])
        }
        let mid = l + ((r - l) >> 1);
        let a = Self::solve(nums, l, mid);
        let b = Self::solve(nums, mid, r);
        if a.is_none() || b.is_none() {
            return a.or(b)
        }
        let mut ans = a.max(b);
        let mut c = 0;
        let mut d = 0;
        for i in (l..mid).rev() {
            c += nums[i];
            d = d.max(c);
        }
        if d == 0 {
            return ans
        }
        c = d;
        for i in mid..r {
            c += nums[i];
            d = d.max(c);
        }
        ans.max(Some(d))
    }
}
