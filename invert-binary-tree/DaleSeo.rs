// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

use std::rc::Rc;
use std::cell::RefCell;

// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.as_ref() {
          let left = node.borrow().left.clone();
          let right = node.borrow().right.clone();

          node.borrow_mut().left = Solution::invert_tree(right);
          node.borrow_mut().right = Solution::invert_tree(left);
        }
        root
    }
}
