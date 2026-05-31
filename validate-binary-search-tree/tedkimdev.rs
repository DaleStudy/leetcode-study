// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

// TC: O(n)
// SC: O(n) - skewed tree
impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
		is_valid(root, i64::MIN, i64::MAX)
    }
}
fn is_valid(node: Option<Rc<RefCell<TreeNode>>>, left: i64, right: i64) -> bool {
	if let Some(n) = node {
		let node_ref = n.borrow();
		let val = node_ref.val as i64;

		if val <= left || val >= right {
			return false;
		}
		return is_valid(node_ref.left.clone(), left, val)
			&& is_valid(node_ref.right.clone(), val, right);
	}
	true
}
