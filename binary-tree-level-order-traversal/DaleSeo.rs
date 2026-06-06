// TC: O(n)
// SC: O(n)
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut output = Vec::new();
        let mut queue = VecDeque::new();
        if let Some(node) = root {
            queue.push_back(node);
        }
        while !queue.is_empty() {
            let mut values = Vec::with_capacity(queue.len());
            for _ in 0..queue.len() {
                let node = queue.pop_front().unwrap();
                let node = node.borrow();
                values.push(node.val);
                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
            output.push(values);
        }
        output
    }
}
