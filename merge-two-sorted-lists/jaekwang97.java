class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                tail.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                tail.next = new ListNode(list2.val);
                list2 = list2.next;
            }

            tail = tail.next;
        }

        while (list1 != null) {
            tail.next = new ListNode(list1.val);
            tail = tail.next;
            list1 = list1.next;
        }

        while (list2 != null) {
            tail.next = new ListNode(list2.val);
            tail = tail.next;
            list2 = list2.next;
        }

        return dummy.next;
    }
}
