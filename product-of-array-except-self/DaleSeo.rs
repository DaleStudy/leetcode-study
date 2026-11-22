// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut products = vec![1; n];

        let mut before = 1;
        for i in 0..n {
            products[i] = before;
            before *= nums[i];
        }

        let mut after = 1;
        for i in (0..n).rev() {
            products[i] *= after;
            after *= nums[i];
        }

        products
    }
}
