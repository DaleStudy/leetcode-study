impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut neg_abs_min = 1;
        let mut total = 1;
        let mut ans = *nums.first()
                .unwrap();
        for num in nums {
            if num == 0 {
                neg_abs_min = 1;
                total = 1;
                ans = ans.max(0);
                continue
            }
            total *= num;
            ans = ans.max(total);
            if total < 0 {
                if neg_abs_min == 1 {
                    neg_abs_min = total;
                } else {
                    ans = ans.max(total / neg_abs_min)
                }
            }
        }
        ans
    }
}
