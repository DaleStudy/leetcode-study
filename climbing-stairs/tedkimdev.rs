// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
		if n <= 2 {
			return n;
		}

		let mut arr: [i32; 2] = [1, 2];
		let mut current = 0;
		for n in 3..=n {
			current = arr[0] + arr[1];
			arr[0] = arr[1];
			arr[1] = current;
		}
		current
    }
}
