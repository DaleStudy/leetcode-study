// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn is_valid(s: String) -> bool {
		let mut stack = Vec::new();

		for c in s.chars() {
			match c {
				'{' | '(' | '[' => {
					stack.push(c);
				},
				'}' => {
					if Some('{') != stack.pop() {
						return false;
					}
				},
				')' => {
					if Some('(') != stack.pop() {
						return false;
					}
				},
				']' => {
					if Some('[') != stack.pop() {
						return false;
					}
				},
				_ => {},
			};
		}

		stack.is_empty()
    }
}
