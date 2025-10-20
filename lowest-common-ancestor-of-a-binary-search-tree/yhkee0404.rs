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
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        match root.as_ref() {
            None => None,
            Some(u) if p.as_ref().map_or(false, |pp| Rc::ptr_eq(u, pp)) => p,
            Some(u) if q.as_ref().map_or(false, |qq| Rc::ptr_eq(u, qq)) => q,
            Some(u) => {
                let u = u.borrow();
                let left = Self::lowest_common_ancestor(u.left.clone(), p.clone(), q.clone());
                let right = Self::lowest_common_ancestor(u.right.clone(), p.clone(), q.clone());
                if left.is_some() && right.is_some() {
                    root.clone()
                } else {
                    left.or(right)
                }
            },
        }
    }
}
