// TC: O(n)
// SC: O(1)
impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let mut len = 0;
        let mut curr = head.as_ref();
        while let Some(node) = curr {
            len += 1;
            curr = node.next.as_ref();
        }
        if len < 3 {
            return;
        }

        let mut tail = {
            let mut node = head.as_mut().unwrap();
            for _ in 0..(len - 1) / 2 {
                node = node.next.as_mut().unwrap();
            }
            node.next.take()
        };

        let mut reversed = None;
        while let Some(mut n) = tail {
            tail = n.next.take();
            n.next = reversed;
            reversed = Some(n);
        }

        let mut node = head.as_mut().unwrap();
        while let Some(mut r) = reversed {
            reversed = r.next.take();
            r.next = node.next.take();
            node.next = Some(r);
            if reversed.is_none() {
                break;
            }
            node = node.next.as_mut().unwrap().next.as_mut().unwrap();
        }
    }
}
