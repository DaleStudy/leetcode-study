impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![1; nums.len()];
        let mut a = 1;
        for i in (0..nums.len()).rev() {
            ans[i] = a * nums[i];
            a = ans[i];
        }
        a = 1;
        for i in 0..nums.len() {
            ans[i] = a * (if i == nums.len() - 1 {1} else {ans[i + 1]});
            a *= nums[i];
        }
        return ans
    }
}
