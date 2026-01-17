public class Geegong {

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode() {}
     *     ListNode(int val) { this.val = val; }
     *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     * }
     */
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode root = new ListNode(Integer.MIN_VALUE, list1);
        ListNode curr1 = list1;
        ListNode curr2 = list2;

        while (curr1 != null && curr2 != null) {
            int val1 = curr1.val;
            int val2 = curr2.val;

            if (val1 <= val2) {
                ListNode temp = curr1.next;
                curr1.next = curr2;
                curr1 = temp;
            } else if (val1 > val2) {
                ListNode temp = curr2.next;
                curr2.next = curr1;
                curr2 = temp;
            }
        }

        return root.next;
    }

    public static class ListNode {
          int val;
          ListNode next;
          ListNode() {}
          ListNode(int val) { this.val = val; }
          ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

}
