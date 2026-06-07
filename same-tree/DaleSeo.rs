// TC: O(n)
// SC: O(n)
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                let a = a.borrow();
                let b = b.borrow();
                a.val == b.val
                    && Self::is_same_tree(a.left.clone(), b.left.clone())
                    && Self::is_same_tree(a.right.clone(), b.right.clone())
            }
            _ => false,
        }
    }
}
