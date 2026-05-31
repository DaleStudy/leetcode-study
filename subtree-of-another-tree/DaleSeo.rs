// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

// LC :O(r × s)
// SC :O(r + s)
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        fn is_same(a: &Option<Rc<RefCell<TreeNode>>>, b: &Option<Rc<RefCell<TreeNode>>>) -> bool {
            match (a, b) {
                (None, None) => true,
                (Some(a), Some(b)) => {
                    let a = a.borrow();
                    let b = b.borrow();
                    a.val == b.val && is_same(&a.left, &b.left) && is_same(&a.right, &b.right)
                }
                _ => false,
            }
        }

        match &root {
            None => sub_root.is_none(),
            Some(node) => {
                if is_same(&root, &sub_root) {
                    return true;
                }
                let node = node.borrow();
                Self::is_subtree(node.left.clone(), sub_root.clone())
                    || Self::is_subtree(node.right.clone(), sub_root.clone())
            }
        }
    }
}
