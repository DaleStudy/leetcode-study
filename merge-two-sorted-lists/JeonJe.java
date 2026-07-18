import java.util.*;

// TC: O(n+m)
// SC: O(n+m)
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                tail.next = new ListNode(list2.val);
                list2 = list2.next;
            } else {
                tail.next = new ListNode(list1.val);
                list1 = list1.next;
            }
            tail = tail.next;
        }

        if (list1 != null) {
            tail.next = list1;
        }

        if (list2 != null) {
            tail.next = list2;
        }

        return dummy.next;
    }
}
