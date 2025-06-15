public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        ListNode cur = head;

        while (cur != null) {
            cur = cur.next;
            length++;
        }

        int start = 1;
        int targetIdx = length - n + 1;
        ListNode result = new ListNode(-1);
        ListNode c = result;

        while (head != null) {
            if (targetIdx == start) {
                head = head.next;
                start++;
                continue;
            }

            c.next = new ListNode(head.val);
            c = c.next;
            start++;
            head = head.next;
        }

        return result.next;
    }
}
