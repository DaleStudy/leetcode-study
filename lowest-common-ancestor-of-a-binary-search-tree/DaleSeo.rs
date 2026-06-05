// TC: O(h)
// SC: O(1)
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p_val = p?.borrow().val;
        let q_val = q?.borrow().val;
        let mut current = root;

        while let Some(node) = current {
            let node_ref = node.borrow();
            if p_val < node_ref.val && q_val < node_ref.val {
                current = node_ref.left.clone();
            } else if p_val > node_ref.val && q_val > node_ref.val {
                current = node_ref.right.clone();
            } else {
                drop(node_ref);
                return Some(node);
            }
        }

        None
    }
}
