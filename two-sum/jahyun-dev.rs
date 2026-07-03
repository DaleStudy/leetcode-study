use std::collections::HashMap;

impl Solution {
    /**
     * Hashmap 사용 시 O(n) 시간 복잡도로 가능하다.
     */
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for i in 0..nums.len() {
            let v = nums[i];
            let r = target - v;

            if let Some(&j) = map.get(&r) {
                return vec![i as i32, j as i32];
            }

            map.insert(v, i as i32);
        }

        return vec![0, 0];
    }

    pub fn two_sum_a(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut idx = [0i32, 2];

        for i in 0..nums.len() {
            for j in (i + 1)..nums.len() {
                if (nums[i] + nums[j]) == target {
                    return vec![i as i32, j as i32];
                }
            }
        }

        return idx.to_vec();
    }
}
