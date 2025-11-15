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
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match &root {
            Some(u) => {
                let u = u.borrow();
                match &sub_root {
                    Some(v) => {
                        let v = v.borrow();
                        Self::solve(root.clone(), sub_root.clone())
                                || Self::is_subtree(u.left.clone(), sub_root.clone())
                                || Self::is_subtree(u.right.clone(), sub_root.clone())
                    },
                    None => false,
                }
            },
            None => sub_root.is_none(),
        }
    }
    fn solve(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            Some(u) => {
                let u = u.borrow();
                match &sub_root {
                    Some(v) => {
                        let v = v.borrow();
                        u.val == v.val
                                && Self::solve(u.left.clone(), v.left.clone())
                                && Self::solve(u.right.clone(), v.right.clone())
                    },
                    None => false,
                }
            },
            None => sub_root.is_none(),
        }
    }
}
