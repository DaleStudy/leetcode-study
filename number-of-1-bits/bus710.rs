#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = Solution::hamming_weight(11);
        assert_eq!(result, 3);
        let result = Solution::hamming_weight(128);
        assert_eq!(result, 1);
        let result = Solution::hamming_weight(2147483645);
        assert_eq!(result, 30);
    }
}

#[derive(Debug)]
struct Solution;

#[allow(dead_code)]
impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let mut cnt: i32 = 0;
        let mut target_bit_holder: i32;

        for i in 0..32 {
            target_bit_holder = n & (0x1 << i);
            if target_bit_holder != 0 {
                cnt += 1;
            }
        }

        cnt
    }
}
