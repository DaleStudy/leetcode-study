// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode::new(0)));
        dummy.as_mut().unwrap().next = head;
        Self::solve(&mut dummy, n);
        dummy.unwrap().next
    }
    fn solve(head: &mut Option<Box<ListNode>>, n: i32) -> i32 {
        match head {
            None => 0,
            Some(u) => {
                let ans = Self::solve(&mut u.next, n) + 1;
                if ans == n + 1 {
                    u.next = u.next.as_mut().unwrap().next.take();
                }
                ans
            }
        }
    }
}
