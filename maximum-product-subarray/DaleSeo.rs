// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut ans = nums[0];
        let (mut max, mut min) = (1, 1);
        for num in nums {
            let candidates = [max * num, min * num, num];
            max = *candidates.iter().max().unwrap();
            min = *candidates.iter().min().unwrap();
            ans = ans.max(max);
        }
        ans
    }
}
