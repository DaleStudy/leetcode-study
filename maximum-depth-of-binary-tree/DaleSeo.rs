// TC: O(n)
// SC: O(n)
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                1 + std::cmp::max(
                    Self::max_depth(node.left.clone()),
                    Self::max_depth(node.right.clone()),
                )
            }
        }
    }
}
