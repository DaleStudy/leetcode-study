// TC: O(m + n)
// SC: O(1)
impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(-1));
        let mut node = &mut dummy;
        let (mut l1, mut l2) = (list1, list2);
        while l1.is_some() && l2.is_some() {
            let val1 = l1.as_ref().unwrap().val;
            let val2 = l2.as_ref().unwrap().val;
            if val1 < val2 {
                node.next = l1;
                node = node.next.as_mut().unwrap();
                l1 = node.next.take();
            } else {
                node.next = l2;
                node = node.next.as_mut().unwrap();
                l2 = node.next.take();
            }
        }
        node.next = l1.or(l2);
        dummy.next
    }
}
