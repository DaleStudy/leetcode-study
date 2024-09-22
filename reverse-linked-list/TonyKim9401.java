// TC: O(n)
// -> visit all elements of head
// SC: O(1)
// -> constant space complexity
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode node = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = node;
            node = head;
            head = temp;
        }
        return node;
    }
}
