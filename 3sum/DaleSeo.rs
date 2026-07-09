// TC: O(n^2)
// SC: O(1)
impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let n = nums.len();
        let mut triplets = Vec::new();

        for i in 0..n {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let (mut low, mut high) = (i + 1, n - 1);
            while low < high {
                let three_sum = nums[i] + nums[low] + nums[high];
                if three_sum < 0 {
                    low += 1;
                } else if three_sum > 0 {
                    high -= 1;
                } else {
                    triplets.push(vec![nums[i], nums[low], nums[high]]);
                    low += 1;
                    high -= 1;
                    while low < high && nums[low] == nums[low - 1] {
                        low += 1;
                    }
                    while low < high && nums[high] == nums[high + 1] {
                        high -= 1;
                    }
                }
            }
        }

        triplets
    }
}
