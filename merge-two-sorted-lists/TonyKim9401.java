// TC: O(n)
// n = length sum of list1 and list2
// SC: O(n)
// n = node 0 ~ length sum of list1 and list2
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode node = new ListNode(0);
        ListNode output = node;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                node.next = list2;
                list2 = list2.next;
            } else {
                node.next = list1;
                list1 = list1.next;
            }
            node = node.next;
        }

        if (list1 == null) node.next = list2;
        if (list2 == null) node.next = list1;

        return output.next;
    }
}
