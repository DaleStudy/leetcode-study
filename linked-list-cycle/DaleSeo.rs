// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn has_cycle(head: Option<Box<ListNode>>) -> bool {
        let mut slow = &head;
        let mut fast = &head;

        while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
            slow = &slow.as_ref().unwrap().next;
            fast = &fast.as_ref().unwrap().next.as_ref().unwrap().next;

            if slow.as_ref().map(|node| node.as_ref() as *const _)
                == fast.as_ref().map(|node| node.as_ref() as *const _)
            {
                return true;
            }
        }

        false
    }
}
