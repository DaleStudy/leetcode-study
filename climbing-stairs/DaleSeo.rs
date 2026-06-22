// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 3 {
            return n;
        }
        let (mut pre, mut cur) = (1, 2);
        for _ in 3..=n {
            let next = pre + cur;
            pre = cur;
            cur = next;
        }
        cur
    }
}
