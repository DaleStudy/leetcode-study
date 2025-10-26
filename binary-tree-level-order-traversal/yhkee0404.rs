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

#[derive(Clone)]
struct QueueItem {
    node: Option<Rc<RefCell<TreeNode>>>,
    dist: i32,
}

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = vec![];
        let mut queue: Vec<QueueItem> = vec![QueueItem::new(root, 0)];
        let mut head = 0;
        while head != queue.len() { // T(n) = S(n) = O(n)
            let u = queue[head].clone();
            head += 1;
            match u.node {
                Some(v) => {
                    let v = v.borrow();
                    let v_dist = u.dist + 1;
                    if ans.len() <= u.dist as usize {
                        ans.push(vec![]);
                    }
                    let mut a = ans.last_mut().unwrap();
                    a.push(v.val);
                    queue.push(QueueItem::new(v.left.clone(), v_dist));
                    queue.push(QueueItem::new(v.right.clone(), v_dist));
                },
                None => (),
            }
        }
        ans
    }
}

impl QueueItem {
    fn new(node: Option<Rc<RefCell<TreeNode>>>, dist: i32) -> Self {
        QueueItem {
            node: node,
            dist: dist,
        }
    }
}
